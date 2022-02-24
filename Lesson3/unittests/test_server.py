import os.path
import sys
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))

from server import process_client_message
from common.variables import PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, ACTION, RESPONDEFAULT_IP_ADDRESSSE

class TestServer(unittest.TestCase):

    err_dict = {
        RESPONDEFAULT_IP_ADDRESSSE: 400,
        ERROR: 'Bad request'
    }
    ok_dict = {RESPONSE: 200}

    def test_ok_check(self):
        # Корректный запрос
        self.assertEqual(process_client_message({ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}),
                         self.ok_dict)

    def test_no_action(self):
        # Ошибка если нет действия
        self.assertEqual(process_client_message({TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}),
                         self.err_dict)

    def test_wrong_action(self):
        # Ошибка если действие не известно
        self.assertEqual(process_client_message({ACTION: 'Wrong', TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}),
                         self.err_dict)

    def test_no_time(self):
        # Ошибка если нет времени
        self.assertEqual(process_client_message({ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}),
                         self.err_dict)

    def test_no_user(self):
        # Ошибка если нет пользователя
        self.assertEqual(process_client_message({ACTION: PRESENCE, TIME: 1.1}),
                         self.err_dict)

    def test_user_not_correct(self):
        # Ошибка если пользователь не известен
        self.assertEqual(process_client_message({ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest123'}}),
                         self.err_dict)

if __name__ == '__main__':
    unittest.main()