#!/usr/bin/env python

from load import load_input


directions = (
    ("^",-1, 0), # up
    (">",0, 1), # right
    ("v",1, 0), # down
    ("<",0, -1), # left
)


def cycle_guard_direction(turn_number):
    return directions[turn_number % len(directions)]


def get_next_position(guard_position, turn_count):
    direction = cycle_guard_direction(turn_count)
    return (
        direction[0],
        (
            guard_position[0] + direction[1],
            guard_position[1] + direction[2]
        )
    )


def find_guard_position(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                return i, j


if __name__ == "__main__":
    grid = load_input()
    guard_position = find_guard_position(grid)
    turn_count = 0
    visited = set()
    char, next_pos = get_next_position(guard_position, turn_count)

    while (
        0 <= next_pos[0] < len(grid) and
        0 <= next_pos[1] < len(grid[0])
    ):
        visited.add(guard_position)
        next_cell = grid[next_pos[0]][next_pos[1]]
        if next_cell in (".", "X"):
            grid[guard_position[0]][guard_position[1]] = "X"
            guard_position = next_pos
        elif next_cell == "#":
            turn_count += 1

        char, next_pos = get_next_position(guard_position, turn_count)
        grid[guard_position[0]][guard_position[1]] = char

    visited.add(guard_position)
    print(len(visited))