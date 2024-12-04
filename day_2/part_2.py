#!/usr/bin/env python

from load import load_input
from safe import safe


def main():
    reports = load_input()
    safe_count = 0

    for report in reports:
        if safe(report, tolerance=1):
            safe_count += 1
        
    print(safe_count)



if __name__ == "__main__":
    main()