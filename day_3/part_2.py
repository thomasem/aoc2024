#!/usr/bin/env python3

from load import load_input
from parse import parse_args_or_none


def parse_arg_pairs(line):
    arg_pairs = []
    enabled = True
    matching = False
    i = 0
    pair_start = 0
    pair_end = 0
    while i < len(line):
        if line[i:i+7] == "don't()":
            enabled = False
            matching = False
            pair_start, pair_end = 0, 0
            i += 7
        if line[i:i+4] == "do()":
            enabled = True
            i += 4

        if not enabled:
            i += 1
            continue

        
        if line[i:i+3] == "mul":
            i += 3
            pair_start = i
            matching = True
        
        if matching and line[i] == ")":
            pair_end = i
            matching = False

        if pair_end - pair_start > 3:
            args = parse_args_or_none(line[pair_start:pair_end+1])
            if args:
                yield args
            pair_start, pair_end = 0, 0

        i += 1


def main():
    arg_pairs = parse_arg_pairs("".join(load_input()))

    sum = 0
    for pair in arg_pairs:
        sum += pair[0] * pair[1]

    print(sum)


if __name__ == "__main__":
    main()
