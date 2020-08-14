import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    payload = req.get_json()
    return func.HttpResponse(f"Received JSON payload {payload}",status_code=200)