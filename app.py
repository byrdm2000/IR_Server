from flask import Flask, request, render_template
from config import Config
import json
import time
from os import listdir
import re
import subprocess

app = Flask(__name__)
app.config.from_object(Config)


def change_color(color):
    """
    Changes color through GPIO
    :param color: String, Color/Button to send to lights
    """
    print("sending", color)
    return subprocess.call(["irsend", "SEND_ONCE", Config.REMOTE, color])


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


@app.route('/')
@app.route('/index')
def index():
    buttons = parse_config()
    # button_styles = {button:Config.BUTTON_HEX_LOOKUP.get(button.lower(), '#a9a9a9') for button in buttons}
    button_styles = Config.BUTTON_HEX_LOOKUP
    shows = listdir('shows')
    return render_template('index.html', title='Home', buttons=buttons, shows=shows, styles=button_styles)


@app.route('/button', methods=["POST"])
def button_handler():
    button = request.form.get("button", None)
    if button:
        change_color(button)
    return index()


@app.route('/show', methods=['POST'])
def show():
    show_file = request.form.get("show_select", None)
    if show_file:
        print("Viewing show", show_file)
        show_file_path = "shows/" + show_file
        with open(show_file_path) as open_show:
            show_data = open_show.read()
        light_show = json.loads(show_data)
        for step in light_show:
            color = step.get('color')
            duration = step.get('duration')
            change_color(color)
            time.sleep(duration)
    return index()


if __name__ == '__main__':
    app.run()
