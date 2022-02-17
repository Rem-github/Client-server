import os.path
import sys
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))

from client import process_ans, create_presence
from common.variables import PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, ACTION




class TestClass(unittest.TestCase):

    # Класс с тестами

    def test_def_presence(self):
        # Тест корректного запроса
        test = create_presence()
        test[TIME] = 1.1  # принудительное выставление времени для возможности теста
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_def_presence_no_user(self):
        # Тест запроса без имени
        test = create_presence()
        test[TIME] = 1.1  # принудительное выставление времени для возможности теста
        self.assertNotEqual(test, {ACTION: PRESENCE, TIME: 1.1})

    def test_def_presence_user_not_correct(self):
        # Тест запроса с не корректным именем
        test = create_presence()
        test[TIME] = 1.1  # принудительное выставление времени для возможности теста
        self.assertNotEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest123'}})


    def test_200_ans(self):
        # Тест на ответ 200
        self.assertEqual(process_ans({RESPONSE: 200}), '200: OK')

    def test_400_ans(self):
        # Тест на ответ 400
        self.assertEqual(process_ans({RESPONSE: 400, ERROR: 'Bad Request'}), '400: Bad Request')

    def test_no_response(self):
        # Тест исключения без поля RESPONSE
        self.assertRaises(ValueError, process_ans, {ERROR: 'Bad Request'})

if __name__ == '__main__':
    unittest.main()