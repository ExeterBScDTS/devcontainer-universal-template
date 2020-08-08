"""Python console app with device flow authentication."""

"""
Attempts to upload large files via the REST API will be met with a 413 response and the message
'The maximum request length supported is 4MB.'

For the solution see
https://docs.microsoft.com/en-us/graph/api/driveitem-createuploadsession?view=graph-rest-1.0

For an example see 
https://keathmilligan.net/automate-your-work-with-msgraph-and-python
"""


import base64
import mimetypes
import os
import urllib
import webbrowser

from adal import AuthenticationContext
import pyperclip
import requests

import pprint

import config

from helpers import api_endpoint, device_flow_session, profile_photo, \
    send_mail, sharing_link, upload_file

def upload_large_file(session, *, filename, folder=None):

    fname_only = os.path.basename(filename)

    # create the Graph endpoint to be used
    if folder:
        # create endpoint for upload to a subfolder
        endpoint = f'me/drive/root:/{folder}/{fname_only}:/createUploadSession'
    else:
        # create endpoint for upload to drive root folder
        endpoint = f'me/drive/root/children/{fname_only}/createUploadSession'

    content_type, _ = mimetypes.guess_type(fname_only)
    result = session.put(api_endpoint(endpoint),
                       json={
            '@microsoft.graph.conflictBehavior': 'replace',
            'description': 'A large test file',
            'fileSystemInfo': {'@odata.type': 'microsoft.graph.fileSystemInfo'},
            'name': fname_only
        })
    
    if result.ok:
        print(result, result.json())
        upload_session = result.json()
        upload_url = upload_session['uploadUrl']

        st = os.stat(filename)
        size = st.st_size
        CHUNK_SIZE = 10485760
        chunks = int(size / CHUNK_SIZE) + 1 if size % CHUNK_SIZE > 0 else 0
        with open(filename, 'rb') as fd:
            start = 0
            for chunk_num in range(chunks):
                chunk = fd.read(CHUNK_SIZE)
                bytes_read = len(chunk)
                upload_range = f'bytes {start}-{start + bytes_read - 1}/{size}'
                print(f'chunk: {chunk_num} bytes read: {bytes_read} upload range: {upload_range}')
                result = requests.put(
                    upload_url,
                    headers={
                        'Content-Length': str(bytes_read),
                        'Content-Range': upload_range
                    },
                    data=chunk
                )
                result.raise_for_status()
                start += bytes_read

    return None

#    content_type, _ = mimetypes.guess_type(fname_only)
#    with open(filename, 'rb') as fhandle:
#        file_content = fhandle.read()
#
#    return session.put(api_endpoint(endpoint),
#                       headers={'content-type': content_type},
#                       data=file_content)


def upload_sample(session):
    """Authenticate user and upload file.

    session = requests.Session() instance with a valid access token for
              Microsoft Graph in its default HTTP headers
    """

    print('\nGet user profile ---------> https://graph.microsoft.com/beta/me')
    user_profile = session.get(api_endpoint('me'))
    print(28*' ' + f'<Response [{user_profile.status_code}]>', f'bytes returned: {len(user_profile.text)}\n')
    if not user_profile.ok:
        pprint.pprint(user_profile.json()) # display error
        return
    user_data = user_profile.json()
    email = user_data['mail']
    display_name = user_data['displayName']

    print(f'Your name ----------------> {display_name}')
    print(f'Your email ---------------> {email}')
  
    file_to_upload = input(f'File to upload (ENTER=README.md) -----> ') or "README.md"
    folder_for_upload = input(f'Folder for upload (ENTER=root) -----> ') or None

    print(f'Upload to OneDrive ------->')
    upload_response = upload_large_file(session, filename=file_to_upload, folder=folder_for_upload)
    print(28*' ' + f'<Response [{upload_response.status_code}]>')
    if not upload_response.ok:
        pprint.pprint(upload_response.json()) # show error message
        return

    response, link_url = sharing_link(session, item_id=upload_response.json()['id'])
    print(28*' ' + f'<Response [{response.status_code}]>',
          f'bytes returned: {len(response.text)}')
    if not response.ok:
        pprint.pprint(response.json()) # show error message
        return

    print('Sharing URL --->', link_url)

if __name__ == '__main__':
    GRAPH_SESSION = device_flow_session(config.CLIENT_ID)
    if GRAPH_SESSION:
        upload_sample(GRAPH_SESSION)
