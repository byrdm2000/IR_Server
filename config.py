class Config:
    SECRET_KEY = 'changme'

    LIRC_REMOTE_CONF_PATH = "Govee_RGB_LED_Remote.lircd.conf"

    REMOTE = LIRC_REMOTE_CONF_PATH.split(".")[0]

    BUTTON_HEX_LOOKUP = {
        'red': '#ff0000',
        'green': '#00ff00',
        'blue': '#0000ff',
        'white': '#ffffff',
    }
