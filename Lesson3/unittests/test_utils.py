import json
import os.path
import sys
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))

from common.utils import get_message, send_message
from common.variables import PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, ACTION, ENCODING

class TestSocket:

    def __init__(self, test_dict):
        self.test_dict = test_dict
        self.encoded_message = None
        self.received_message = None

    def send(self, message_to_send):

        json_test_message = json.dumps(self.test_dict)
        self.encoded_message = json_test_message.encode(ENCODING)
        self.received_message = message_to_send

    def recv(self, max_len):

        json_test_message = json.dumps(self.test_dict)
        return json_test_message.encode(ENCODING)

class TestUtils(unittest.TestCase):

    test_dict_send = {
        ACTION: PRESENCE,
        TIME: 111111.111111,
        USER: {
            ACCOUNT_NAME: 'test_user'
        }
    }
    test_dict_recv_ok = {RESPONSE: 200}
    test_dict_recv_err = {
        RESPONSE: 400,
        ERROR: 'Bad request'
    }

    def test_send_message_true(self):

        test_socket = TestSocket(self.test_dict_send)
        send_message(test_socket, self.test_dict_send)
        self.assertEqual(test_socket.encoded_message, test_socket.received_message)

    def test_send_message_false(self):
        test_socket = TestSocket(self.test_dict_send)
        send_message(test_socket, 'wrong_dict')
        self.assertNotEqual(test_socket.encoded_message, test_socket.received_message)

    def test_get_message_ok_dict(self):
        test_sock_ok = TestSocket(self.test_dict_recv_ok)
        self.assertEqual(get_message(test_sock_ok), self.test_dict_recv_ok)

    def test_get_message_err_dict(self):
        test_sock_err = TestSocket(self.test_dict_recv_err)
        self.assertEqual(get_message(test_sock_err), self.test_dict_recv_err)

if __name__ == '__main__':
    unittest.main()