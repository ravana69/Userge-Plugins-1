""" Battery Status """

# By @Krishna_Singhal moded by @r4v4n4

from pyrogram.errors.exceptions.bad_request_400 import YouBlockedUser
from userge import Message, userge
from userge.utils.exceptions import StopConversation


@userge.on_cmd(
    "b1",
    about={
        "header": "@rn5pbot gives information of my First Phone",
        "flags": {"No Flag"},
        "usage": "{tr}b1 [Reply to user]",
    },
)
async def buttery1_(message: Message):
    """ Get User's Phone Status"""
    replied = message.reply_to_message
    if not replied:
        await message.err("```Reply to get Battery Status...```", del_in=5)
        return
    user = replied.from_user.id
    chat = "@rn5pbot"
    await message.edit("```Getting Battery information of First Phone```")
    msgs = []
    ERROR_MSG = "For your kind information, you blocked @rn5pbot, Unblock it"
    try:
        async with userge.conversation(chat) as conv:
            try:
                await conv.send_message("/battery {}".format(user))
            except YouBlockedUser:
                await message.err(f"**{ERROR_MSG}**", del_in=5)
                return
            msgs.append(await conv.get_response(mark_read=True))
            msgs.append(await conv.get_response(mark_read=True))
            msgs.append(await conv.get_response(timeout=3, mark_read=True))
    except StopConversation:
        pass
    battery1 = "Battery"
    username = "Username History"
    for msg in msgs:
        if "-u" in message.flags:
            if msg.text.startswith("No records found"):
                await message.edit("```User never changed his Username...```", del_in=5)
                return
            if msg.text.startswith(username):
                await message.edit(f"`{msg.text}`")
        else:
            if msg.text.startswith("No records found"):
                await message.edit("```User never changed his Name...```", del_in=5)
                return
            if msg.text.startswith(battery1):
                await message.edit(f"`{msg.text}`")



@userge.on_cmd(
    "b2",
    about={
        "header": "@rn5pbot gives information of my First Phone",
        "flags": {"No Flag"},
        "usage": "{tr}b2 [Reply to user]",
    },
)
async def buttery2_(message: Message):
    """ Get User's Phone Status"""
    replied = message.reply_to_message
    if not replied:
        await message.err("```Reply to get Battery Status...```", del_in=5)
        return
    user = replied.from_user.id
    chat = "@ravanaphonebot"
    await message.edit("```Getting Battery information of Second Phone```")
    msgs = []
    ERROR_MSG = "For your kind information, you blocked @ravanaphonebot, Unblock it"
    try:
        async with userge.conversation(chat) as conv:
            try:
                await conv.send_message("/battery {}".format(user))
            except YouBlockedUser:
                await message.err(f"**{ERROR_MSG}**", del_in=5)
                return
            msgs.append(await conv.get_response(mark_read=True))
            msgs.append(await conv.get_response(mark_read=True))
            msgs.append(await conv.get_response(timeout=3, mark_read=True))
    except StopConversation:
        pass
    battery2 = "Battery"
    username = "Username History"
    for msg in msgs:
        if "-u" in message.flags:
            if msg.text.startswith("No records found"):
                await message.edit("```User never changed his Username...```", del_in=5)
                return
            if msg.text.startswith(username):
                await message.edit(f"`{msg.text}`")
        else:
            if msg.text.startswith("No records found"):
                await message.edit("```User never changed his Name...```", del_in=5)
                return
            if msg.text.startswith(battery2):
                await message.edit(f"`{msg.text}`")