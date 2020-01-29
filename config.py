class Config:
    SECRET_KEY = 'changme'

    BUTTON_SIGNAL_LOOKUP = {
        'red': 0,
        'green': 2,
        'blue': 1,
        'white': 3,
    }

    BUTTON_HEX_LOOKUP = {
        'red': '#ff0000',
        'green': '#00ff00',
        'blue': '#0000ff',
        'white': '#ffffff',
    }

    COLORS = BUTTON_SIGNAL_LOOKUP.keys()
