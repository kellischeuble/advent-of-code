def parse_rules(file: str) -> dict:
    """
    Iterates through file creating a dictionary of all of the rules
    with the color of bags being the key, and the set of bags that it can
    contain being the values
    """
    with open(file, "r") as rules:
        rule_dict = dict()
        for rule in rules:
            rule = rule.split("contain")
            color = rule[0].rpartition(" bags ")[0]
            rule_dict[color] = set()
            can_contain = rule[1].split(",")
            for rule_color in can_contain:
                rule_dict[color].add(rule_color[3:].rpartition(" ")[0])
    return rule_dict

def check_bag_contains_gold(color: str, current_bag: str, rules: dict) -> bool:
    """
    Checks bag color, and all of the bags inside of that bag (recursively) to 
    see if it eventually can contain a gold bag.

    Args:
        color (str): color of bag to check for ("shiny gold") in this example
        current_bag (str): outer bag color
        rules (dict): dictionary containing the rules

    Returns:
        bool: True if bag can eventually hold the color. False if not
    """
    if color in rules[current_bag]:
        return True
    # TODO: this needs to be changed, but for now if a bag contains no 
    # other bags the rule_dict has a value of " other"
    if rules[current_bag] == {" other"}:
        return False
    contains = False
    for contents in rules[current_bag]:
        if check_bag_contains_gold(color, contents, rules):
            contains = True
    if contains:
        return True

def count_bags_contain_gold(rule_dict: dict) -> int:
    """
    Iterates through all of the colors to see if they, as the outermost
    bag, can contain gold
    """
    no_of_bags = 0
    for color in list(rule_dict.keys()):
        if not color == "shiny gold":
            if check_bag_contains_gold("shiny gold", color, rule_dict):
                no_of_bags += 1
    return no_of_bags

if __name__ == "__main__":
    rule_dict = parse_rules("rules.txt")
    print(len(rule_dict.keys()))
    bags = count_bags_contain_gold(rule_dict)
    print("Answer to part one: ", bags)


#rule_dict = {"bright white": ["shiny gold"], "muted yellow": ["shiny gold"], "dark orange": ["bright white", "muted yellow"], "light red": ["bright white", "muted yellow"]}