#!/usr/bin/env python

from load import load_input

def pop_smallest(locations):
    smallest_index = 0
    for i in range(len(locations)):
        if locations[i] < locations[smallest_index]:
            smallest_index = i
    return locations.pop(smallest_index)

def main():
    a, b = load_input()
    distance = 0
    while len(a) > 0 and len(b) > 0:
        smallest_a = pop_smallest(a)
        smallest_b = pop_smallest(b)
        distance += abs(smallest_a - smallest_b)
    print(distance)

if __name__ == "__main__":
    main()