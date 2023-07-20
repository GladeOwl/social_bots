"""Telegram Bot Module"""

import asyncio

import requests
import telegram
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


def get_secret(token: str):
    """Gets the secret for the token from the API"""
    response: requests.Response = requests.get(
        "http://api:6000/secret", json={"token": token}, timeout=10
    )
    return response.text.replace('"', "")


TOKEN: str = get_secret("telegram")
USERID: str = get_secret("telegram-user-id")


class Request(BaseModel):
    """Message Data Class"""

    message: str


def start_bot():
    """Starts the Telegram Bot"""

    return telegram.Bot(TOKEN)


@app.get("/")
async def main():
    """Get API Status"""
    return True


@app.post("/send")
def send(request: Request):
    """Accept API input and pass it to the Bot"""
    return asyncio.run(send_message(request.message))


async def send_message(message):
    """Send Message via the Telegram Bot"""
    bot: telegram.Bot = start_bot()

    async with bot:
        await bot.send_message(chat_id=USERID, text=message)
    return "Message Sent"
