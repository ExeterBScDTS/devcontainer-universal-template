import logging

import azure.functions as func

import subprocess
import tempfile

def main(req: func.HttpRequest, audioBlob: func.InputStream, videoBlob: func.InputStream, outputBlob: func.Out[func.InputStream]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    #name = req.get_json()['Audio']['FileName']

    outFile = tempfile.NamedTemporaryFile(suffix='.mkv')

    audioFile = tempfile.NamedTemporaryFile(suffix='.ogg')
    audioData = audioBlob.read(-1)
    audioFile.write(audioData)
    audioLen = len(audioData)

    videoFile = tempfile.NamedTemporaryFile(suffix='.webm')
    videoData = videoBlob.read(-1)
    videoFile.write(videoData)
    videoLen = len(videoData)

    # As outFile now exists use -y option to ffmpeg to allow overwriting of this zero length file
    result = subprocess.run(['ffmpeg', '-y', '-i', audioFile.name, '-i', videoFile.name, '-acodec', 'copy', '-vcodec', 'copy', outFile.name], capture_output=True)
    logging.info(result.stderr)

    #data = outFile.read(-1)
    outputBlob.set(outFile)
    datalen = 0 #len(data)

    return func.HttpResponse(f"All done {audioLen} {datalen}",status_code=200)