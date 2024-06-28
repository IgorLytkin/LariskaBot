import aiogram
import logging
from pathlib import Path

from lariska_bot.handlers.handler import *

logger = logging.getLogger(__name__)
def main():
    log_name = f'/logs/{datetime.now().strftime("%Y-%m-%d")}.log'
    Path(log_name).parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(level=logging.DEBUG,filename=log_name,filemode="a")

    logger.info('Запуск бота')
    logger.debug('Пишем сообщения в ' + log_name)
    logger.debug('Запуск опроса')
    start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    main()
