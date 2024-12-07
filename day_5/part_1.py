#!/usr/bin/env python

from load import load_input
from rules import to_rules_lookup



def check_update(rules_lookup, update):
    for i in range(len(update)):
        page = update[i]
        for page_before in update[:i]:
            if page_before in rules_lookup.get(page, []):
                return False
    return True


if __name__ == "__main__":
    rules, updates = load_input()
    rules_lookup = to_rules_lookup(rules)
    sum_of_middle = 0
    for update in updates:
        if check_update(rules_lookup, update):
            sum_of_middle += int(update[len(update) // 2])
    print(sum_of_middle)
