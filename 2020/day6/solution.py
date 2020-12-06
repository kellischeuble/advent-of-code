def part_one():
    with open("answers.csv", "r") as answers:

        group = set()
        no_of_unique_answers = []

        for answer in answers:
            for char in answer:
                group.add(char)
            if answer == "\n":
                group = group - {"\n"}
                print(group)
                no_of_unique_answers.append(len(group))
                group = set()
        group = group - {"\n"}
        no_of_unique_answers.append(len(group))
        print(group)
        print(no_of_unique_answers)

    sum = 0 

    for no in no_of_unique_answers:
        sum += no

    return sum

def part_two():
    with open("answers.txt", "r") as answers:
        groups_responses = list()
        all_same = list()

        for answer in answers:
            print("ANSWER", answer)
            if not answer == "\n":
                groups_responses.append(answer.split("\n")[0])
            print("GROUPS_RESPONSES", groups_responses)
            if answer == "\n":
                groups_responses = list()
        groups_responses.append(answer.split("\n"))  

    counts = 0

    for group in groups_responses:
        group_letters = set()
        group = 1
        for letter in groups_responses[0]:
            while group < len(groups_responses):
                is_in = True
                if letter not in groups_responses[group]:
                    is_in = False
            if is_in:
                group_letters.add(letter)



part_two()


