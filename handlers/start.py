from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f""" Hello ❤️ {message.from_user.first_name}! I can play music in voice chats of Telegeam Groups. I have a lot of cool feature that will amaze you!\n\n★ Do you want me to play music in your Telegram groups'voice chats? Please click the " Command " button below to know how you can use me.\n\n★ Use the buttons below to know more about me ❤️\n\n★ Contact my owner [╰‿╯ᴮᴬᴰ᭄ S H I N C H A N](https://t.me/Mafia_Shinchan_Op)""",
       

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "〽️ Source code", url="https://github.com/Shinchan-xD/Marshmallo-Music"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/Liebe_Support"
                    ),
                    InlineKeyboardButton(
                        "Channel 🔈", url="https://t.me/xD_Bots"
                    ),
                   
                ],
                [
                    InlineKeyboardButton(
                        "Commands ‼️", url="https://telegra.ph/%F0%92%86%9C%E1%8F%95%E1%8F%82%E1%8E%A5%E1%8F%81%E1%8D%88%E1%8F%82%E1%8F%97%E1%8F%81-%F0%9D%95%8B%F0%9D%95%96%F0%9D%95%92%F0%9D%95%9E-PERRY-GANG%F0%92%86%9C-04-28-3"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "🥺 Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Yea 🔥", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No 🤧", callback_data="close"
                    )
                ]
            ]
        )
    )
