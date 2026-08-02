from pyrogram import filters
from 999music import app
from 999music.utils.colored_buttons import (
    styled_button,
    buttons_to_inline_markup,
    smart_send_photo as send_photo_colored,
)
from config import BOT_USERNAME

repo_caption = """**
🚀 ᴄʟᴏɴᴇ ᴀɴᴅ ᴅᴇᴘʟᴏʏ – 🚀

➤ ᴅᴇᴘʟᴏʏ ᴇᴀsɪʟʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴇʀʀᴏʀꜱ  
➤ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪꜱꜱᴜᴇ  
➤ ɴᴏ ɪᴅ ʙᴀɴ ɪꜱꜱᴜᴇ   
➤ ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏꜱ  
➤ ʀᴜɴ 24/7 ʟᴀɢ ꜰʀᴇᴇ

ɪꜰ ʏᴏᴜ ꜰᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ, ꜱᴇɴᴅ ꜱꜱ ɪɴ ꜱᴜᴘᴘᴏʀᴛ
**"""

@app.on_message(filters.command("repo"))
async def show_repo(_, msg):
    buttons = [
        [styled_button("➕ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✨", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [
            styled_button("👑 ᴏᴡɴᴇʀ", url="https://t.me/+hCDkQp9TNwIxNzI1"),
            styled_button("💬 ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/+OqS-RsnNrMtjOTll"),
        ],
        [
            styled_button("🛠️ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/+JmZajlpyTJxlZTE1"),
            styled_button("🎵 ", url="https://t.me/+73UOpH8smTplYTE9"),
        ],
    ]

    try:
        await send_photo_colored(
            chat_id=msg.chat.id,
            photo="https://i.ibb.co/0VnyqcDm/x.jpg",
            caption=repo_caption,
            reply_markup=buttons,
        )
    except:
        pass
