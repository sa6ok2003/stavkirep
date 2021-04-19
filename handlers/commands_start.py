from aiogram import types
from misc import dp,bot

id1 = 749831385
id2 = 1288245739

chat_id = -1001434261031


@dp.message_handler(content_types=['text','voice','video_note'])
async def cmd_start(message: types.Message):
    if (message.chat.id == id1) or (message.chat.id ==id2):
        await bot.copy_message(chat_id=chat_id,from_chat_id=message.chat.id,message_id=message.message_id)