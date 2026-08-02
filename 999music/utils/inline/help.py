from 999music import app
from 999music.utils.colored_buttons import styled_button


TOTAL_SECTIONS = 29

# Alternate button colors: green → blue → green → blue ...
_STYLE_CYCLE = ["success", "primary"]


def generate_help_buttons(_, start: int, end: int, current_page: int):
    """Return category buttons with alternating green/blue colors."""
    buttons, per_row = [], 3
    for idx, i in enumerate(range(start, end + 1)):
        if idx % per_row == 0:
            buttons.append([])
        style = _STYLE_CYCLE[idx % len(_STYLE_CYCLE)]
        buttons[-1].append(
            styled_button(
                text=_[f"H_B_{i}"],
                callback_data=f"help_callback hb{i}_p{current_page}",
                
            )
        )
    return buttons


def first_page(_):
    buttons = generate_help_buttons(_, 1, 15, current_page=1)
    # Menu = blue, Next = green (positive)
    buttons.append(
        [
            styled_button(text="๏ ᴍᴇɴᴜ ๏", callback_data="back_to_main"),
            styled_button(text="๏ ɴᴇxᴛ ๏", callback_data="help_next_2"),
        ]
    )
    return buttons


def second_page(_):
    buttons = generate_help_buttons(_, 16, TOTAL_SECTIONS, current_page=2)
    # Back = blue, Menu = green
    buttons.append(
        [
            styled_button(text="๏ ʙᴀᴄᴋ ๏", callback_data="help_prev_1"),
            styled_button(text="๏ ᴍᴇɴᴜ ๏", callback_data="back_to_main"),
        ]
    )
    return buttons


def action_sub_menu(_, current_page: int):
    return [
        [
            styled_button(text=_["H_B_S_1"], callback_data="action_prom_1"),
            styled_button(text=_["H_B_S_2"], callback_data="action_pun_1"),
        ],
        [
            styled_button(text=_["BACK_BUTTON"], callback_data=f"help_back_{current_page}"),
        ],
    ]


def help_back_markup(_, current_page: int):
    return [
        [
            styled_button(text=_["BACK_BUTTON"], callback_data=f"help_back_{current_page}"),
            styled_button(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]


def private_help_panel(_):
    return [
        [
            styled_button(text=_["S_B_3"], url=f"https://t.me/{app.username}?start=help"),
        ],
    ]
