import json
import os
import sys


sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import MAX_PACKAGE_LENGTH, ENCODING
from decos import log
from errors import IncorrectDataRecivedError, NonDictInputError

@log
def get_message(client):

    encode_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encode_response, bytes):
        json_response = encode_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        else:
            raise IncorrectDataRecivedError
    else:
        raise IncorrectDataRecivedError


@log
def send_message(sock, message):
    if not isinstance(message,dict):
        raise NonDictInputError
    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)
