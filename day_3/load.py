import os


_dir = os.path.dirname(os.path.abspath(__file__))


def load_input():
    lines = []
    with open(os.path.join(_dir, "input.txt")) as f:
        lines = f.readlines()
    return lines