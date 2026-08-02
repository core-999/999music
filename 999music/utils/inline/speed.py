from 999music.utils.colored_buttons import styled_button


def speed_markup(_, chat_id):
    buttons = [
        [
            styled_button(text="🕒 0.5x", callback_data=f"SpeedUP {chat_id}|0.5"),
            styled_button(text="🕓 0.75x", callback_data=f"SpeedUP {chat_id}|0.75"),
        ],
        [
            styled_button(text=_["P_B_4"], callback_data=f"SpeedUP {chat_id}|1.0"),
        ],
        [
            styled_button(text="🕤 1.5x", callback_data=f"SpeedUP {chat_id}|1.5"),
            styled_button(text="🕛 2.0x", callback_data=f"SpeedUP {chat_id}|2.0"),
        ],
        [
            styled_button(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons
