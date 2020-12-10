from typing import Dict, List

from passport import Passport


def parse_file(file: str) -> List[Dict]:
    """
    Returns a list of all passports to validate
    Each passport is in its own dictionary
    """
    with open(file, "r") as raw_passports:
        passports_list = list()
        passport = dict()

        for line in raw_passports:
            if line == "\n":
                passports_list.append(passport)
                passport = dict()

            current = line.split()
            for info in current:
                # first 3 chars are the field, 4th char is a ":"
                passport[info[:3]] = info[4:]
        # add last passport at the end because there isn't a \n after
        passports_list.append(passport)
    return passports_list


def verify_correct_fields(passport_dict):
    """
    for part one
    """
    FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
    return set(passport_dict.keys()) == FIELDS or set(
        passport_dict.keys()
    ) == FIELDS - {"cid"}


def create_passport_objects(passports_list: List[Dict]) -> List[Passport]:
    """
    Goes over the list of raw passports to be validated.
    First checks to see if the correct fields are there. 
    TODO: Remove this into its own function
    Then loads info into Passport object and adds to list
    """
    passport_objects = list()
    count_correct_fields = 0
    for passport in passports_list:
        if verify_correct_fields(passport):
            count_correct_fields += 1
            loaded_passport = Passport(
                byr=passport["byr"],
                iyr=passport["iyr"],
                eyr=passport["eyr"],
                hgt=passport["hgt"],
                hcl=passport["hcl"],
                ecl=passport["ecl"],
                pid=passport["pid"],
            )
            passport_objects.append(loaded_passport)

    return passport_objects, count_correct_fields


def validate_all_passports(passports: List[Passport]) -> int:
    """
    Counts the number of valid passports

    Args:
        passports (list[Passport]): list of Passport objects

    Returns:
        int: number of valid passports
    """
    count = 0
    for passport in passports:
        if passport.validate_passport():
            count += 1
    return count


if __name__ == "__main__":
    passport_list = parse_file("data/passport_data.txt")
    passport_objects, fields = create_passport_objects(passport_list)
    print("PART 1:", fields)
    print("PART 2:", validate_all_passports(passport_objects))
