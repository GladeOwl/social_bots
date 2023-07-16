"""Telegram Bot Module"""

import asyncio
import os

import telegram
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()
app = FastAPI()

TOKEN = os.getenv("TOKEN")
USERID = os.getenv("USERID")


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
    bot = start_bot()
    async with bot:
        await bot.send_message(chat_id=USERID, text=message)
    return "Message Sent"
