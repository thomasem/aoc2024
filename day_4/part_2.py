#!/usr/bin/env python

from load import load_input


x_mases = [
    (
        ["S", "*", "S"],
        ["*", "A", "*"],
        ["M", "*", "M"],
    ),
    (
        ["M", "*", "M"],
        ["*", "A", "*"],
        ["S", "*", "S"],
    ),
    (
        ["S", "*", "M"],
        ["*", "A", "*"],
        ["S", "*", "M"],
    ),
    (
        ["M", "*", "S"],
        ["*", "A", "*"],
        ["M", "*", "S"],
    )
]


def contains_x_mas(grid):
    for combination in x_mases:
        matched = True
        for i in range(len(combination)):
            for j in range(len(combination[i])):
                if combination[i][j] == "*":
                    continue
                if grid[i][j] != combination[i][j]:
                    matched = False
                    break
        if matched:
            return True


def extract_3_x_3_around(grid, i, j):
    return [
        grid[i-1][j-1:j+2],
        grid[i][j-1:j+2],
        grid[i+1][j-1:j+2],
    ]


def main():
    grid = load_input()
    sum = 0
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if grid[i][j] == "A":
                if contains_x_mas(extract_3_x_3_around(grid, i, j)):
                    sum += 1

    print(sum)


if __name__ == "__main__":
    main()

