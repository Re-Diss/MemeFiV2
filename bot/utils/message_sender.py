from pyrogram import Client
from pyrogram.errors import Unauthorized, UserDeactivated, AuthKeyUnregistered

from bot.exceptions import InvalidSession


async def send_message(tg_client: Client, msg: str):
    if not tg_client.is_connected:
        try:
            await tg_client.connect()
            await tg_client.send_message('memefi_coin_bot', msg)
            await tg_client.disconnect()
        except (Unauthorized, UserDeactivated, AuthKeyUnregistered):
            raise InvalidSession(tg_client.name)


class MessageSender:
    pass