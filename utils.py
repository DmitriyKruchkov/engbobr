import re

import aiohttp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import FOLDER_ID, API_KEY, STREAM, TEMPERATURE, MAX_TOKEN, GPT_URL
from core import creator
from prompts import WORD_PROMT, SYSTEM_PROMT


def escape_markdown_v2(text):
    # Экранирование всех специальных символов для MarkdownV2
    escape_chars = r'\_[]()~`>#+-={}.!'
    return re.sub(r'([%s])' % re.escape(escape_chars), r'\\\1', text)


def get_word():
    return creator.word()


def make_row_keyboard(items):
    row = [KeyboardButton(text=item) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)


async def word_request():
    headers = {
        "Content-Type": "application/json",
        'Authorization': f'Api-Key {API_KEY}',
    }
    body = {
        "modelUri": f"gpt://{FOLDER_ID}/yandexgpt-lite",
        "completionOptions": {
            "stream": STREAM,
            "temperature": TEMPERATURE,
            "maxTokens": MAX_TOKEN
        },
        "messages": [

            {
                "role": "user",
                "text": WORD_PROMT + get_word()

            }
        ]
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(GPT_URL, headers=headers, json=body) as response:
            response = await response.json()
            result = response["result"]["alternatives"][0]["message"]["text"]
            result = list(filter(lambda x: x, result.split("\n")))
            answer = '\n'.join(result[:4]) + "\n||" + '\n'.join(result[4:]) + "||"
            return answer


async def sentence_checker(text):
    headers = {
        "Content-Type": "application/json",
        'Authorization': f'Api-Key {API_KEY}',
    }
    body = {
        "modelUri": f"gpt://{FOLDER_ID}/yandexgpt-lite",
        "completionOptions": {
            "stream": STREAM,
            "temperature": TEMPERATURE + 0.3,
            "maxTokens": MAX_TOKEN
        },
        "messages": [
            {
                "role": "system",
                "text": SYSTEM_PROMT

            },
            {
                "role": "user",
                "text": text

            }
        ]
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(GPT_URL, headers=headers, json=body) as response:
            response = await response.json()
            result = response["result"]["alternatives"][0]["message"]["text"]
            return result
