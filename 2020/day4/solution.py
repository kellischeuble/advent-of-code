from passport import Passport

def parse_file(file):
    with open(file, "r") as raw_passports:
        passport_list = list()
        passport = dict()

        for line in raw_passports:
            if line == "\n":
                passport_list.append(passport)

            current = line.split()
            for info in current:
                passport[info[:3]] = info[4:]
        # very last one isn't going to have a newline char after it
        passport_list.append(passport)
    return passport_list

def create_passport_objects(passports_list):
    passport_objects = list()

    for passport in passports_list:
        if set(passport.keys()) == {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"} or set(passport.keys()) == {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}:
            loaded_passport = Passport(byr=passport["byr"], iyr=passport["iyr"], eyr=passport["eyr"], hgt=passport["hgt"], hcl=passport["hcl"], ecl=passport["ecl"], pid=passport["pid"])
            passport_objects.append(loaded_passport)
    
    return passport_objects

def validate_all_passports(passports):
    count = 0
    for passport in passports:
        if passport.validate_passport():
            count += 1
    return count

if __name__ == "__main__":
    passport_list = parse_file("passport_data.txt")
    passport_objects = create_passport_objects(passport_list)
    print(validate_all_passports(passport_objects))
