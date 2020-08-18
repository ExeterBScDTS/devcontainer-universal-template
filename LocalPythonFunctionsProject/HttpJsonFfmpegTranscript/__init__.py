import logging

import azure.functions as func

import subprocess
import tempfile

def main(req: func.HttpRequest, 
audioBlob: func.InputStream, videoBlob: func.InputStream, 
transcriptBlob: func.InputStream,
outputBlob: func.Out[func.InputStream]) -> func.HttpResponse:

    outFile = tempfile.NamedTemporaryFile(suffix='.mkv')

    audioFile = tempfile.NamedTemporaryFile(suffix='.ogg')
    audioData = audioBlob.read(-1)
    audioFile.write(audioData)

    videoFile = tempfile.NamedTemporaryFile(suffix='.webm')
    videoData = videoBlob.read(-1)
    videoFile.write(videoData)

    transcriptFile = tempfile.NamedTemporaryFile(suffix='.srt')
    transcriptFile.write(transcriptBlob.read(-1))

    # As outFile now exists use -y option to ffmpeg to allow overwriting of this zero length file
    result = subprocess.run(['ffmpeg', '-y', '-i', audioFile.name, '-i', videoFile.name, 
    '-f', 'srt', '-i', transcriptFile.name, '-acodec', 'copy', '-vcodec', 'copy', 
    '-c:s', 'srt', outFile.name], capture_output=True)
    #logging.info(result.stderr)

    outputBlob.set(outFile)

    return func.HttpResponse(f"All done",status_code=200)