def to_rules_lookup(rules):
    rules_lookup = {}
    for rule in rules:
        rule_entry = rules_lookup.get(rule[0], [])
        rules_lookup[rule[0]] = rule_entry + [rule[1]]
    return rules_lookup
