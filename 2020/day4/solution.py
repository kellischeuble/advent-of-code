from passport import Passport

def parse_file(file):
    with open(file, "r") as raw_passports:
        passports_list = list()
        passport = dict()

        for line in raw_passports:
            if line == "\n":
                passports_list.append(passport)
                passport = dict()

            current = line.split()
            for info in current:
                passport[info[:3]] = info[4:]
        # very last one isn't going to have a newline char after it
        passports_list.append(passport)
    return passports_list

def verify_correct_fields(passport_dict):
    """
    for part one
    """
    return (set(passport_dict.keys()) == {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}) or (set(passport_dict.keys()) == {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"})

def create_passport_objects(passports_list):
    passport_objects = list()
    count_correct_fields = 0
    for passport in passports_list:
        if verify_correct_fields(passport):
            count_correct_fields += 1
            loaded_passport = Passport(byr=passport["byr"], iyr=passport["iyr"], eyr=passport["eyr"], hgt=passport["hgt"], hcl=passport["hcl"], ecl=passport["ecl"], pid=passport["pid"])
            passport_objects.append(loaded_passport)
    
    return passport_objects, count_correct_fields

def validate_all_passports(passports):
    count = 0
    for i, passport in enumerate(passports):
        if passport.validate_passport():
            count += 1
    return count

if __name__ == "__main__":
    passport_list = parse_file("data/passport_data.txt")
    passport_objects, fields = create_passport_objects(passport_list)
    print("PART 1:", fields)
    print("PART 2:", validate_all_passports(passport_objects))