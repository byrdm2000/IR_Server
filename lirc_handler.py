import re
from config import Config


def parse_config():
    """
    Parses the LIRC config file
    :return: List, of all buttons specified in LIRC
    """
    buttons = []
    with open(Config.LIRC_REMOTE_CONF_PATH) as lirc_conf:
        for line in lirc_conf:
            m = re.match('^\s*(\S*)\s*(?=0x00)', line)  # matches lines with 0x00 in them, puts non-whitespace in group
            if m is not None:
                buttons.append(m.group(1))
    return buttons
