def safe_brute(report):
    diffs = [report[i+1] - report[i] for i in range(len(report) - 1)]
    return all(0 < diff < 4 for diff in diffs) or all(-4 < diff < 0 for diff in diffs)


def safe_brute_dampener(report):
    if safe_brute(report):
        return True
    
    for i in range(len(report)):
        if safe_brute(report[:i] + report[i+1:]):
            return True 

    return False


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
            # because it's the value that sets the trend;
            # also try removing this value and the next one
            return safe(report[1:], tolerance - 1) \
                or safe(report[:i] + report[i + 1:], tolerance - 1) \
                or safe(report[:i+1] + report[i + 2:], tolerance - 1)

    return True