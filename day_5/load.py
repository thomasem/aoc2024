def load_input():
    lines = []
    rules = []
    updates = []
    with open("input.txt") as f:
        lines = f.readlines()
    for line in lines:
        if line == '\n':
            continue
        if "|" in line:
            rules.append(line.strip().split("|"))
        else:
            updates.append(line.strip().split(","))
    return rules, updates