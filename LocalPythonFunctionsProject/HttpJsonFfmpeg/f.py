import logging

import subprocess
import tempfile


audio = open('tmp/recording.ogg', 'rb')
audioFile = tempfile.NamedTemporaryFile(suffix='.ogg')
audioFile.write(audio.read(-1))

video = open('tmp/recording.webm', 'rb')
videoFile = tempfile.NamedTemporaryFile(suffix='.webm')
videoFile.write(video.read(-1))


outFile = tempfile.NamedTemporaryFile(suffix='.mkv')
# As outFile now exists use -y option to ffmpeg to allow overwriting of this zero length file
subprocess.call(['ffmpeg', '-y', '-i', audioFile.name, '-i', videoFile.name, '-acodec', 'copy', '-vcodec', 'copy', outFile.name])

data = outFile.read()
print(len(data))
