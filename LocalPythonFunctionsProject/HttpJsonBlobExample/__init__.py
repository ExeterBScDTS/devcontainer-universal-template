import logging

import azure.functions as func


def main(req: func.HttpRequest, audioBlob: func.InputStream, videoBlob: func.InputStream) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.get_json()['Audio']['FileName']
    data_bytes = audioBlob.read(-1)
    nbytes = len(data_bytes)
    return func.HttpResponse(f"Hello {nbytes} read from {name}",status_code=200)