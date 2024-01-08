"""Discord Bot API module"""

import requests
import threading
import hikari
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

APP = FastAPI()


def get_secret(token: str):
    """Gets the secret for the token from the API"""
    response: requests.Response = requests.get(
        "http://api:6000/secret", json={"token": token}, timeout=10
    )
    return response.text.replace('"', "")


TOKEN: str = get_secret("discord")
USERID: str = get_secret("discord-user-id")

BOT = hikari.GatewayBot(token=TOKEN)


def start_api():
    try:
        uvicorn.run(APP, host="0.0.0.0", port=5001)
    except Exception:
        print("API was closed.")


class Request(BaseModel):
    """Message Data Class"""

    message: str


@APP.get("/")
async def main():
    """Get API Status"""
    return True


@APP.get("/send")
async def send(request: Request):
    """Send message to user"""
    print(request.message)
    await send_message(request.message)


async def send_message(message: str):
    """Pass the Message to the Bot"""
    user: hikari.users.User = await BOT.rest.fetch_user(USERID)
    print(user.id)
    await user.send(content=message)


def run_bot():
    BOT.run()


threading.Thread(target=run_bot, daemon=True).start()
start_api()
