from passport_fields import (
    BirthYear,
    IssueYear,
    ExpirationYear,
    Height,
    HairColor,
    EyeColor,
    PassportID,
    CountryID,
)


class Passport:

    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid=None):
        self.byr = BirthYear(byr)
        self.iyr = IssueYear(iyr)
        self.eyr = ExpirationYear(eyr)
        self.hgt = Height(hgt)
        self.hcl = HairColor(hcl)
        self.ecl = EyeColor(ecl)
        self.pid = PassportID(pid)
        self.cid = CountryID(cid)

    def validate_passport(self):
        return (
            self.byr.validate()
            and self.iyr.validate()
            and self.eyr.validate()
            and self.hgt.validate()
            and self.hcl.validate()
            and self.ecl.validate()
            and self.pid.validate()
        )

    def __repr__(self):
        return (
            f"byr: {self.byr}\niyr: {self.iyr}\neyr: {self.eyr}\nhgt: {self.hgt}\nhcl: {self.hcl}\necl: {self.ecl}\npid: {self.pid}\ncid: {self.cid}"
        )
