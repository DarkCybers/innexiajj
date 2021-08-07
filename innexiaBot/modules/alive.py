# COPYRIGHT (C) 2021 @useIes

from telethon import events, Button, custom
import re, os
from innexiaBot.events import register
from innexiaBot import telethn as tbot
from innexiaBot import telethn as tgbot
from innexiaBot import (SUPPORT_CHAT, OWNER_USERNAME)

PHOTO = "https://telegra.ph/file/00dca1590296efc1956e0.jpg"
@register(pattern=("/alive"))
async def awake(event):
  innexiaXname = event.sender.first_name
  innexiaX = f"**👋 Hᴇʟʟᴏ {innexiaXname}, I Aᴍ Iɴɴᴇxɪᴀ**\n\n"
  innexiaX += "🔸 `I Aᴍ Wᴏʀᴋɪɴɢ Pʀᴏᴘᴇʀʟʏ`\n"
  innexiaX += "🔹 `Iɴɴᴇxɪᴀ Oꜱ : 2.0 Lᴀᴛᴇꜱᴛ`\n"
  innexiaX += f"🔸 `Mʏ Mᴀꜱᴛᴇʀ` @useIes\n"
  innexiaX += "🔹 `I'ᴍ Uᴘᴅᴀᴛᴇᴅ`\n"
  innexiaX += "🔸 `Tᴇʟᴇᴛʜᴏɴ : 1.19.5 Lᴀᴛᴇꜱᴛ`\n"
  innexiaX += "**🥰 Tʜᴀɴᴋ Yᴏᴜ Fᴏʀ Aᴅᴅ Mᴇ Hᴇʀᴇ!**"
  BUTTON = [[Button.url("Sᴜᴘᴘᴏʀᴛ", f"https://t.me/{SUPPORT_CHAT}"), Button.url("Oᴡɴᴇʀ", f"https://t.me/{OWNER_USERNAME}")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=innexiaX,  buttons=BUTTON)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"innexiaX")))
async def callback_query_handler(event):
# inline by @useIes 🔥
  sammy = [[Button.url("REPO", "https://github.com/DarkCybers"), Button.url("REPO-INNEXIA", "https://github.com/DarkCybers/Innexia")]]
  sammy +=[[Button.url("SUPPORT CHANNEL", "https://t.me/SiderzBot"), Button.url("SUPPORT GROUP", "https://t.me/SiderzChat")]]
  sammy +=[[custom.Button.inline("ALIVE", data="sammy")]]
  await event.edit(text=f"ALL DETAILS OF REPOS", buttons=sammy)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"sammy")))
async def callback_query_handler(event):
  global PHOTO
  innexiaXname = event.sender.first_name
  innexiaX = f"**👋 Hᴇʟʟᴏ {innexiaXname}, I Aᴍ Iɴɴᴇxɪᴀ**\n\n"
  innexiaX += "🔸 `I Aᴍ Wᴏʀᴋɪɴɢ Pʀᴏᴘᴇʀʟʏ`\n"
  innexiaX += "🔹 `Iɴɴᴇxɪᴀ Oꜱ : 2.0 Lᴀᴛᴇꜱᴛ`\n"
  innexiaX += f"🔸 `Mʏ Mᴀꜱᴛᴇʀ` @useIes\n"
  innexiaX += "🔹 `I'ᴍ Uᴘᴅᴀᴛᴇᴅ`\n"
  innexiaX += "🔸 `Tᴇʟᴇᴛʜᴏɴ : 1.19.5 Lᴀᴛᴇꜱᴛ`\n"
  innexiaX += "**🥰 Tʜᴀɴᴋ Yᴏᴜ Fᴏʀ Aᴅᴅ Mᴇ Hᴇʀᴇ!**"
  BUTTON = [[Button.url("Sᴜᴘᴘᴏʀᴛ", f"https://t.me/{SUPPORT_CHAT}"), Button.url("Oᴡɴᴇʀ", f"https://t.me/{OWNER_USERNAME}")]]
  await event.edit(text=InnexiaX, buttons=BUTTONS)
