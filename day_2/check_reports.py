#!/usr/bin/env python

import sys

from load import load_input


def safe(report, tolerance=0):
    if tolerance < 0:
        return False

    trend = None
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]

        if trend is None:
            trend = diff

        if abs(diff) > 3 or diff == 0 or trend * diff < 0:
            # handle edge case where first value needs to be removed
            # and try removing this value and the next one
            return safe(report[1:], tolerance - 1) \
                or safe(report[:i] + report[i + 1:], tolerance - 1) \
                or safe(report[:i+1] + report[i + 2:], tolerance - 1)

    return True


def main():
    reports = load_input()
    safe_count = 0

    tolerance = 0
    if (len(sys.argv) > 1):
        tolerance = int(sys.argv[1])

    for report in reports:
        if safe(report, tolerance=tolerance):
            safe_count += 1

    print(safe_count)


if __name__ == "__main__":
    main()