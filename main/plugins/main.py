

import time, os

from .. import bot as Beast

from config import Config

from .. import userbot, Bot

from functions.forcesub import handle_force_subscribe

from main.plugins.pyroplug import get_msg

from telethon import events

from telethon.tl.types import DocumentAttributeVideo

from ethon.pyfunc import video_metadata

from ethon.telefunc import fast_upload, fast_download, force_sub

from main.plugins.helpers import get_link, join, screenshot


@Beast.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))

async def clone(update, bot):

    if Config.UPDATES_CHANNEL:
      fsub = await handle_force_subscribe(update, bot)
    if fsub == 400:
        return
    if update.is_reply:

        return

    try:

        link = get_link(update.text)

        if not link:

            return

    except TypeError:

        return

    edit = await update.reply("Processing!")

    if 't.me/+' in link:

        print('+ in link')

        q = await join(userbot, link)

        await edit.edit(q)

        return 

    if 't.me/' in link:

        print('- in link')

        await get_msg(userbot, Bot, event.sender_id, edit.id, link, 0)

        

