import json
import logging
import socket
import sys
from errors import IncorrectDataRecivedError
import logs.config_server_log


from common.utils import get_message, send_message
from common.variables import *

SERVER_LOGGER = logging.getLogger('server')

def process_client_message(message):

    SERVER_LOGGER.debug(f'Разбор сообщения от клиента: {message}')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message \
        and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONDEFAULT_IP_ADDRESSSE: 400,
        ERROR: 'Bad request'
    }

def main():

    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p')+1])
        else:
            listen_port = DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            SERVER_LOGGER.critical(f'Попытка запуска сервера с указанием неподходящего порта '
                                   f'{listen_port}. Допустимы адреса с 1024 до 65535')
            raise ValueError
    except IndexError:
        SERVER_LOGGER.error(f'{sys.argv} не содержит -\'p\' ')
        sys.exit(1)
    except ValueError:
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a')+1]
        else:
            listen_address = ''
    except IndexError:
        SERVER_LOGGER.error(f'После параметра \'-а\' - необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)
    SERVER_LOGGER.info(f'Запущен сервер: {listen_port}, '
                       f'Адрес, с которого принимаются подключения: {listen_address}, '
                       f'Если адрес не указан, принимаются соединения с любых адресов.')

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    transport.bind((listen_address, listen_port))
    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        SERVER_LOGGER.info(f'Установлено соединение с ПК: {client_address}')
        try:
            message_from_client = get_message(client)
            SERVER_LOGGER.info(f'Получено сообщение: {message_from_client}')
            response = process_client_message(message_from_client)
            SERVER_LOGGER.info(f'Сформирован ответ клиенту: {response}')
            send_message(client, response)
            SERVER_LOGGER.debug(f'Соединение с клиентом {client_address} закрывается')
            client.close()
        except json.JSONDecodeError:
            SERVER_LOGGER.error(f'Не удалось декодировать JSON строку от клиента {client_address}. '
                                f'Соединение закрывается')
            client.close()
        except IncorrectDataRecivedError:
            SERVER_LOGGER.error(f'От клиента {client_address} приняты не корректные данные.'
                                f'Соединение закрывается.')


if __name__ == '__main__':
    main()
