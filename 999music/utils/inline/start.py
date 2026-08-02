import config
from 999music import app
from 999music.utils.colored_buttons import styled_button


def start_panel(_):
    # Add me = success (green, positive CTA), Channel = primary (blue, info)
    buttons = [
        [
            styled_button(text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"),
            styled_button(text=_["S_B_2"], url=config.SUPPORT_CHANNEL),
        ],
    ]
    return buttons


def private_panel(_):
    # Add me = success (green CTA), Owner + Support = primary (blue), Help = success (green)
    buttons = [
        [
            styled_button(text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"),
        ],
        [
            styled_button(text=_["S_B_2"], url=config.SUPPORT_CHANNEL),
            styled_button(text=_["S_B_4"], url=config.SUPPORT_CHAT),
        ],
        [
            styled_button(text=_["S_B_3"], callback_data="open_help"),
        ],
    ]
    return buttons
