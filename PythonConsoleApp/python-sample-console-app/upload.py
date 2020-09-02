"""Python console app with device flow authentication."""
# Copyright (c) Microsoft. All rights reserved. Licensed under the MIT license.
# See LICENSE in the project root for license information.
import pprint

import config

from helpers import api_endpoint, device_flow_session, profile_photo, \
    send_mail, sharing_link, upload_file

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
    upload_response = upload_file(session, filename=file_to_upload, folder=folder_for_upload)
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
