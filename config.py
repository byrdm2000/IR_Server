import re


class LircConfig:
    LIRC_REMOTE_CONF_PATH = "Govee_RGB_LED_Remote.lircd.conf"

    REMOTE = LIRC_REMOTE_CONF_PATH.split(".")[0]


def parse_config():
    """
    Parses the LIRC config file
    :return: List, of all buttons specified in LIRC
    """
    buttons = []
    with open(LircConfig.LIRC_REMOTE_CONF_PATH) as lirc_conf:
        for line in lirc_conf:
            m = re.match('^\s*(\S*)\s*(?=0x00)', line)  # matches lines with 0x00 in them, puts non-whitespace in group
            if m is not None:
                buttons.append(m.group(1))
    return buttons


class Config:
    SECRET_KEY = 'changme'

    BUTTON_HEX_LOOKUP = {
        'red': '#ff0000',
        'green': '#00ff00',
        'blue': '#0000ff',
        'white': '#ffffff',
    }

    COLORS = parse_config()
