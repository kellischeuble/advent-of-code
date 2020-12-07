def split_into_groups(unparsed_file: str) -> list:
    groups = unparsed_file.split("\n\n")
    return groups

def find_unique_answers_per_group(group: list) -> int:
            chars = set()
            for letter in group:
                if not letter == "\n":
                    chars.add(letter)   
            return len(chars)

def count_similar_answers(group: list) -> int:
    chars = set()
    for char in group[0]:
        word_in_all = True
        for word in group[1:]:
            if char not in word and not word == "":
                word_in_all = False
        if word_in_all:
            chars.add(char)
    return len(chars)

def split_group(group: list) -> list:
    return group.split("\n")

def part_one(groups: list) -> int:
    sum = 0
    for group in groups:
        sum += find_unique_answers_per_group(group)
    return sum

def part_two(groups: list) -> int:
    sum = 0
    for group in groups:
        people = split_group(group)
        sum += count_similar_answers(people)
    return sum

if __name__ == "__main__":
    with open("answers.txt", "r") as answers:
        groups = split_into_groups(answers.read())

    print("ANSWER TO PART ONE: ", part_one(groups))
    print("ANSWER TO PART TWO: ", part_two(groups))



