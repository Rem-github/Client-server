import logging
from datetime import date
from logging.handlers import TimedRotatingFileHandler

log = logging.getLogger('server')
formatter = logging.Formatter('%(asctime)s - %(levelname)s -%(name)s - %(message)s ')
current_date = date.today()
file_hand = TimedRotatingFileHandler(
    f'server.log.{current_date}', when="D", interval=1, backupCount=5
)
file_hand.setFormatter(formatter)
log.addHandler(file_hand)
log.setLevel(logging.DEBUG)

if __name__ == '__main__':
    stream_hand = logging.StreamHandler()
    stream_hand.setFormatter(formatter)
    log.addHandler(stream_hand)
    log.debug('Отладочное сообщение')