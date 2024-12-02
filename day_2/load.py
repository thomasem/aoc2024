import os


_dir = os.path.dirname(os.path.abspath(__file__))


def parse_report_string(report_string):
    levels = []
    for level_string in report_string.strip().split(" "):
        levels.append(int(level_string.strip()))
    return levels


def load_input():
    lines = []
    reports = []
    with open(os.path.join(_dir, "input.txt")) as f:
        lines = f.readlines()
    for line in lines:
        reports.append(parse_report_string(line))
    return reports