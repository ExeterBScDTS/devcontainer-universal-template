
import subprocess
import tempfile
import json


result = subprocess.run(['docker', 'ps', '-q'], capture_output=True, encoding='utf-8')
containerId = result.stdout.strip()

result = subprocess.run(['docker', 'inspect', '--format="{{json .Mounts}}', containerId], capture_output=True, encoding='utf-8')
containerInfo = json.loads( result.stdout[1:].strip() )

print(containerInfo[0]['Source'], containerInfo[0]['Destination'])

#hostDir = containerInfo['Labels']['vsch.local.folder']
#print("DIR", hostDir)

hostdir='/home/mike/github/ExeterBScDTS/devcontainer-universal-template/ffmpeg/samples'

audioFileName='recording.ogg'

videoFileName='recording.webm'

outFileName='recording.mkv'

result = subprocess.run(['docker', 'run', '--user', '1000:1000', 
'-v', f'{hostdir}:/tmp/workdir', '-w', '/tmp/workdir',
        'jrottenberg/ffmpeg', 
        '-i', audioFileName, '-i', videoFileName, 
        '-acodec', 'copy', '-vcodec', 'copy', 
        outFileName], capture_output=True)

print(result.stderr)

