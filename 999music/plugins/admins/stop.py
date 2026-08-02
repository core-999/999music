from pyrogram import filters
from pyrogram.types import Message

from 999music import app
from 999music.core.call import VISHAL
from 999music.utils.database import set_loop
from 999music.utils.decorators import AdminRightsCheck
from 999music.utils.colored_buttons import buttons_to_inline_markup
from 999music.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(
    filters.command(["end"], prefixes=["/", "!"]) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await VISHAL.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        text=_["admin_5"].format(message.from_user.mention),
        reply_markup=buttons_to_inline_markup(close_markup(_))
    )
