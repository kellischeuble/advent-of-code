# TODO:
# also thinking it might make sense to have the rules
# be their own classes so that I don't have to write the functions over and
# over again...


class BirthYear:
    rule_length = 4
    rule_min_year = 1920
    rule_max_year = 2002

    def __init__(self, byr):
        self.byr = byr

    def validate(self):
        byr_int = int(self.byr)
        if (
            len(self.byr) == self.rule_length
            and byr_int >= self.rule_min_year
            and byr_int <= self.rule_max_year
        ):
            return True
        return False

    def __repr__(self):
        return f"{self.byr}"


class IssueYear:
    rule_length = 4
    rule_min_year = 2010
    rule_max_year = 2020

    def __init__(self, iyr):
        self.iyr = iyr

    def validate(self):
        iyr_int = int(self.iyr)
        if (
            len(self.iyr) == self.rule_length
            and iyr_int >= self.rule_min_year
            and iyr_int <= self.rule_max_year
        ):
            return True
        return False

    def __repr__(self):
        return f"{self.iyr}"


class ExpirationYear:
    rule_length = 4
    rule_min_year = 2020
    rule_max_year = 2030

    def __init__(self, eyr):
        self.eyr = eyr

    def validate(self):
        eyr_int = int(self.eyr)
        return (
            len(self.eyr) == self.rule_length
            and eyr_int >= self.rule_min_year
            and eyr_int <= self.rule_max_year
        )

    def __repr__(self):
        return f"{self.eyr}"


class Height:
    rule_ends_with = {"cm", "in"}
    rule_if_cm_min = 150
    rule_if_cm_max = 193
    rule_if_in_min = 59
    rule_if_in_max = 76

    def __init__(self, hgt):
        self.hgt = hgt

    def validate(self):
        if len(self.hgt) <= 2:
            return False
        hgt_int = int(self.hgt[:-2])

        def if_cm():
            return hgt_int >= self.rule_if_cm_min and hgt_int <= self.rule_if_cm_max

        def if_in():
            return hgt_int >= self.rule_if_in_min and hgt_int <= self.rule_if_in_max

        if self.hgt[-2:] == "cm":
            return if_cm()
        elif self.hgt[-2:] == "in":
            return if_in()
        return False

    def __repr__(self):
        return f"{self.hgt}"


class HairColor:
    rule_starts_with = "#"
    rule_can_only_contain = {
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
    }

    def __init__(self, hcl):
        self.hcl = hcl

    def validate(self):

        if self.hcl[0] == self.rule_starts_with:
            for char in self.hcl[1:]:
                if char not in self.rule_can_only_contain:
                    return False, f"Incorrect Hair Color with {self.hcl}"
            return True
        return False

    def __repr__(self):
        return f"{self.hcl}"


class EyeColor:
    rule_can_only_contain = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    def __init__(self, ecl):
        self.ecl = ecl

    def validate(self):
        return self.ecl in self.rule_can_only_contain

    def __repr__(self):
        return f"{self.ecl}"


class PassportID:
    rule_length = 9

    def __init__(self, pid):
        self.pid = pid

    def validate(self):
        return self.pid.isdigit() and len(self.pid) == self.rule_length

    def __repr__(self):
        return f"{self.pid}"


class CountryID:

    def __init__(self, cid):
        self.cid = cid

    def validate(self):
        return True

    def __repr__(self):
        return f"{self.cid}"
