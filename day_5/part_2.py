#!/usr/bin/env python

from load import load_input
from rules import to_rules_lookup


def ensure_corrected(rules_lookup, update):
    corrected = False
    copy = update.copy()
    i, j = 1, 0
    while i < len(copy) and i > 0:
        j = 0
        while j < i:
            page_before = copy[j]
            if page_before in rules_lookup.get(copy[i], []):
                corrected = True
                del copy[j]
                copy.insert(i + 1, page_before)
                i -= 1
            else:
                j += 1
        i += 1
    return corrected, copy


if __name__ == "__main__":
    rules, updates = load_input()
    rules_lookup = to_rules_lookup(rules)
    corrected_sum_of_middle = []
    for update in updates:
        corrected, correct = ensure_corrected(rules_lookup, update)
        if corrected:
            corrected_sum_of_middle.append(int(correct[len(correct) // 2]))
    print(sum(corrected_sum_of_middle))