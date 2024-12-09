def load_input():
    lines = []
    with open("input.txt") as f:
        lines = f.readlines()
    return [list(line.strip()) for line in lines]