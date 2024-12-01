#!/usr/bin/env python

import os


_dir = os.path.dirname(os.path.abspath(__file__))

def load_input():
    lines = []
    a, b = [], []
    with open(os.path.join(_dir, "input.txt")) as f:
        lines = f.readlines()
    for line in lines:
        left, right = line.split()
        a.append(int(left.strip()))
        b.append(int(right.strip()))
    return a, b