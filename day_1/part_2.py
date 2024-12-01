#!/usr/bin/env python

from load import load_input

def count_occurrences(locations, value):
    count = 0
    for i in range(len(locations)):
        if locations[i] == value:
            count += 1
    return count

def main():
    a, b = load_input()
    similarity = 0
    for location in a:
        similarity += location * count_occurrences(b, location)
    print(similarity)

if __name__ == "__main__":
    main()