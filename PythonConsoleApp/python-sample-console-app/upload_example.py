import requests
import msal
import atexit
import os.path
import urllib.parse
import os


TENANT_ID = '<your tenant id>'
CLIENT_ID = '<your application id>'
SHAREPOINT_HOST_NAME = 'yourcompany.sharepoint.com'
SITE_NAME = '<your site name>'

AUTHORITY = 'https://login.microsoftonline.com/' + TENANT_ID
ENDPOINT = 'https://graph.microsoft.com/v1.0'

SCOPES = [
    'Files.ReadWrite.All',
    'Sites.ReadWrite.All',
    'User.Read',
    'User.ReadBasic.All'
]

cache = msal.SerializableTokenCache()

if os.path.exists('token_cache.bin'):
    cache.deserialize(open('token_cache.bin', 'r').read())

atexit.register(lambda: open('token_cache.bin', 'w').write(cache.serialize()) if cache.has_state_changed else None)

app = msal.PublicClientApplication(CLIENT_ID, authority=AUTHORITY, token_cache=cache)

accounts = app.get_accounts()
result = None
if len(accounts) > 0:
    result = app.acquire_token_silent(SCOPES, account=accounts[0])

if result is None:
    flow = app.initiate_device_flow(scopes=SCOPES)
    if 'user_code' not in flow:
        raise Exception('Failed to create device flow')

    print(flow['message'])

    result = app.acquire_token_by_device_flow(flow)

if 'access_token' in result:
    access_token = result['access_token']
    headers={'Authorization': 'Bearer ' + access_token}

    # get the site id
    result = requests.get(f'{ENDPOINT}/sites/{SHAREPOINT_HOST_NAME}:/sites/{SITE_NAME}', headers=headers)
    result.raise_for_status()
    site_info = result.json()
    site_id = site_info['id']

    # get the drive id
    result = requests.get(f'{ENDPOINT}/sites/{site_id}/drive', headers=headers)
    result.raise_for_status()
    drive_info = result.json()
    drive_id = drive_info['id']

    # upload a large file to the 'General' folder -- replace these
    filename = 'Large File.pdf'
    folder_path = 'General'

    folder_url = urllib.parse.quote(folder_path)
    result = requests.get(f'{ENDPOINT}/drives/{drive_id}/root:/{folder_url}', headers=headers)
    result.raise_for_status()
    folder_info = result.json()
    folder_id = folder_info['id']

    file_url = urllib.parse.quote(filename)
    result = requests.post(
        f'{ENDPOINT}/drives/{drive_id}/items/{folder_id}:/{file_url}:/createUploadSession',
        headers=headers,
        json={
            '@microsoft.graph.conflictBehavior': 'replace',
            'description': 'A large test file',
            'fileSystemInfo': {'@odata.type': 'microsoft.graph.fileSystemInfo'},
            'name': filename
        }
    )
    result.raise_for_status()
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

else:
    raise Exception('no access token in result')
