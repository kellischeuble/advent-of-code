def split_input(input: str) -> tuple:
    """
    Splits the input into the letter being searched for,
    The lower required letter count, the upper required 
    letter count, and the password to verify
    """
    parts = input.split()

    letter = parts[1][0]
    password = parts[2]

    ranges = parts[0].split("-")
    lower_range = int(ranges[0])
    upper_range = int(ranges[1])

    return lower_range, upper_range, letter, password


def verify_pass_part_one(password: str) -> bool:
    """
    Verifies password with the conditions that the specified
    letter must be within the lower and upper range count.
    """
    lower_range, upper_range, letter, password = split_input(password)

    count = 0
    for item in password:
        if item == letter:
            count += 1
            if count > upper_range:
                return False
    if count < lower_range:
        return False
    return True


def count_valid_pass_part_one(file):
    """
    Counts the number of valid passwords in file 
    """
    with open(file, "r") as passwords:

        valid_passwords = 0

        for password in passwords:
            if verify_pass_part_one(password):
                valid_passwords += 1

        return valid_passwords


def verify_pass_part_two(password: str) -> bool:
    """
    Verifies password with the condition that there must
    be a letter at one, and only one, of the given two indices
    """
    pos_one, pos_two, letter, password = split_input(password)

    one = password[pos_one - 1] == letter
    two = password[pos_two - 1] == letter

    if one and two:
        return False
    if not one and not two:
        return False
    return True


def count_valid_pass_part_two(file):
    """     
    Counts the number of valid passwords in file
    """
    with open(file, "r") as passwords:

        valid_passwords = 0

        for password in passwords:
            if verify_pass_part_two(password):
                valid_passwords += 1

        return valid_passwords


if __name__ == "__main__":
    print("ANSWER TO PART ONE:", count_valid_pass_part_one("passwords.csv"))
    print("ANSWER TO PART TWO:", count_valid_pass_part_two("passwords.csv"))
