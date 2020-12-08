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

def parse_rules_part_two(file: str) -> dict:
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
            rule_dict[color] = dict()
            can_contain = rule[1].split(",")
            for rule_color in can_contain:
                number = rule_color[1]
                if number == "n":
                    number = 0
                rule_dict[color][(rule_color[3:].rpartition(" ")[0])] = int(number)
    return rule_dict

rule_dict = parse_rules_part_two("rules.txt")

# def count_bags_in_gold(cur_color="shiny gold", level_above=1, total=0):
#     for required_bag in rule_dict[cur_color]:
#         if required_bag == " other":
#             return total
#         no = rule_dict[cur_color][required_bag]
#         total += (no * level_above)
#         return count_bags_in_gold(required_bag, no*level_above, total)

def count_bags_in_gold(rule_dict):
    queue = list()

    for key, value in rule_dict["shiny gold"].items():
        queue.append([key, value, 1])

    total = 0

    while len(queue) > 0:
        current = queue.pop(0)
        current_color, current_no, prev = current[0], current[1], current[2]
        total += (prev * current_no)
        for key, value in rule_dict[current_color].items():
            if not key == " other":
                queue.append([key, value, current_no])
    return total          

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
    rule_dict_part_one = parse_rules("rules.txt")
    bags = count_bags_contain_gold(rule_dict_part_one)
    print("Answer to part one: ", bags)

    rule_dict_part_two = parse_rules_part_two("rules.txt")
    bags = count_bags_in_gold(rule_dict_part_two)
    print("Answer to part two: ", bags)