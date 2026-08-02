from 999music.utils.colored_buttons import styled_button


def stats_buttons(_, status):
    not_sudo = [
        styled_button(text=_["SA_B_1"], callback_data="TopOverall"),
    ]
    sudo = [
        styled_button(text=_["SA_B_2"], callback_data="bot_stats_sudo"),
        styled_button(text=_["SA_B_3"], callback_data="TopOverall"),
    ]
    return [
        sudo if status else not_sudo,
        [
            styled_button(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]


def back_stats_buttons(_):
    return [
        [
            styled_button(text=_["BACK_BUTTON"], callback_data="stats_back"),
            styled_button(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
