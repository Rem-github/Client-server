import logging

log = logging.getLogger('client')
formatter = logging.Formatter('%(asctime)s - %(levelname)s -%(name)s - %(message)s ')
file_hand = logging.FileHandler('client.log', encoding='utf-8')
file_hand.setFormatter(formatter)
log.addHandler(file_hand)
log.setLevel(logging.DEBUG)

if __name__ == '__main__':
    stream_hand = logging.StreamHandler()
    stream_hand.setFormatter(formatter)
    log.addHandler(stream_hand)
    log.debug('Отладочное сообщение')