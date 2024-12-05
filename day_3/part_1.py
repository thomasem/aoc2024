#!/usr/bin/env python

from load import load_input
from parse import parse_args_or_none


def parse_arg_pairs(line):
    # split on 'mul' command
    # if open paren, match numbers until comma
    # match numbers until close paren
    parts = line.split('mul')
    for part in parts:
        args = parse_args_or_none(part)
        if args:
            yield args


def main():
    arg_pairs = []
    for line in load_input():
        arg_pair = parse_arg_pairs(line)
        if arg_pair:
            arg_pairs.extend(arg_pair)
    
    sum = 0
    for pair in arg_pairs:
        sum += pair[0] * pair[1]

    print(sum)



if __name__ == '__main__':
    main()