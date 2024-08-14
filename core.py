import logging
import faker
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import TG_API

bot = Bot(token=TG_API)
dp = Dispatcher(storage=MemoryStorage())
creator = faker.Faker()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)
