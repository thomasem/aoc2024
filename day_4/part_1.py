#!/usr/bin/env python3

from load import load_input


xmas = ["X", "M", "A", "S"]
directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]


def check_direction(grid, i, j, word, offset):
    word_copy = word.copy()
    while 0 <= i < len(grid) and 0 <= j < len(grid[i]):
        if grid[i][j] == word_copy[0]:
            word_copy.pop(0)
            if len(word_copy) == 0:
                return 1
            i += offset[0]
            j += offset[1]
        else:
            break
    return 0


def find_xmas(grid):
    i = 0
    count = 0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            if grid[i][j] == xmas[0]:
                count += sum(
                    check_direction(grid, i, j, xmas, direction)
                    for direction in directions
                )
            j += 1
        i += 1
    return count


def main():
    grid = load_input()
    count = find_xmas(grid)
    print(count)


if __name__ == "__main__":
    main()