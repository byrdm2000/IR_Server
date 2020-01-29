from config import Config
import json
from os import listdir


class Step(object):
    def __init__(self, color, duration):
        """
        Initializes a step object
        :param color: Color of light step, must be in the colors in config.py
        :param duration: Duration of this color
        """
        if color not in Config.COLORS:
            raise ValueError
        else:
            self.color = color
            self.duration = duration

    def __repr__(self):
        return {'color': self.color, 'duration': self.duration}


class Show(object):
    def __init__(self):
        self.steps = []

    def __repr__(self):
        return [x.__repr__() for x in self.steps]

    def pretty_print(self):
        index = 1
        for step in self.steps:
            print(index, step.color, "-", step.duration, "sec")
            index += 1

    def add_step(self, step):
        """
        Adds step to show
        :param step: Step object
        """
        self.steps.append(step)

    def remove_step(self, index):
        """
        Removes step based on index
        Steps are 1-index
        """
        actual_index = index - 1
        self.steps.pop(actual_index)  # add OutOfBounds handling

    def insert_step(self, index, step):
        actual_index = index - 1
        self.steps.insert(actual_index, step)


edit_option = None
while edit_option is None or edit_option not in {"1", "2"}:
    edit_option = input("Welcome to light show editor! Select an option: \n"
                        "1. Create new show\n"
                        "2. Edit existing show\n"
                        "Option: ")
    if edit_option not in {"1", "2"}:
        print("Invalid input")

show_file = None
if edit_option == "1":
    # Create new show
    show_file = input("Filename: ")
    show_to_edit = Show()
else:
    # Load existing show
    show_to_edit = None
    while show_to_edit is None:
        print("Pick show:")
        shows = listdir('shows')
        for show in shows:
            print(show)
        show_file = input("Filename: ")
        if show_file not in shows:
            print("Invalid input")
        else:
            with open("shows/" + show_file) as show:
                show_data = show.read()
            show_list = json.loads(show_data)
            print(show_list)
            show_to_edit = Show()
            for dict_step in show_list:
                step_step = Step(dict_step['color'], dict_step['duration'])
                show_to_edit.add_step(step_step)


# Main loop
def make_step():
    """
    Makes step object
    """
    color = input("Pick color: ")
    duration = float(input("Duration: "))
    return Step(color, duration)


def list_to_serial(L):
    """
    basically removes the brackets
    """
    elements_string = ""
    for index in range(len(L)):
        if index == len(L) - 1:  # last index:
            elements_string += str(L[index])
        else:
            elements_string += str(L[index]) + ", "
    return elements_string


editor_commands = ['add', 'remove', 'insert', 'save', 'colors', 'quit', 'help']
editor_option = None
while editor_option is None or editor_option in editor_commands and editor_option != 'quit':
    show_to_edit.pretty_print()
    editor_option = input("Command: ")
    if editor_option not in editor_commands and editor_option is not None:
        print("Invalid input")
        editor_option = None
    elif editor_option == 'add':
        show_to_edit.add_step(make_step())
    elif editor_option == 'remove':
        index = int(input("Index: "))
        show_to_edit.remove_step(index)
    elif editor_option == 'insert':
        index = int(input("Index: "))
        show_to_edit.insert_step(index, make_step())
    elif editor_option == 'save':
        json_string = json.dumps(show_to_edit.__repr__())
        with open("shows/" + show_file, 'x') as show_to_save:
            show_to_save.write(json_string)
        print("File saved")
    elif editor_option == 'help':
        print("Commands:", list_to_serial(editor_commands))
    elif editor_option == 'colors':
        print("Colors:", list_to_serial(list(Config.COLORS)))
