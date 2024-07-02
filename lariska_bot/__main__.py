import logging
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from lariska_bot import TOKEN

logger = logging.getLogger(__name__)
storage = MemoryStorage()
dp = Dispatcher() # Подготовка диспетчера


if __name__ == '__main__':
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
    # Инициализируем бот и диспетчер
    logger.debug('Инициализируем бот')
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
    logger.debug('Бот инициализирован')

    logger.info('Запуск бота')
    logger.debug('Запускаем диспетчер')
    dp.run_polling(bot)