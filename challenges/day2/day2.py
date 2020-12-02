""" 
PART ONE:
---------
Your flight departs in a few days from the coastal airport; the easiest way down 
to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. 
"Something's wrong with our computers; we can't log in!" You ask if you can 
take a look.

Their password database seems to be a little corrupted: some of the passwords 
wouldn't have been allowed by the Official Toboggan Corporate Policy that was 
in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of 
passwords (according to the corrupted database) and the corporate policy when 
that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy 
indicates the lowest and highest number of times a given letter must appear for 
the password to be valid. For example, 1-3 a means that the password must contain 
a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; 
it contains no instances of b, but needs at least 1. The first and third passwords 
are valid: they contain one a or nine c, both within the limits of their respective 
policies.

How many passwords are valid according to their policies?
"""

def split_input(input: str):
    
    parts = input.split()

    letter = parts[1][0]
    password = parts[2]

    ranges = parts[0].split("-")
    lower_range = int(ranges[0])
    upper_range = int(ranges[1])

    return lower_range, upper_range, letter, password


def is_valid(password: str) -> bool:
    """
    Looks at constraints password and to see if it is valid

    Args:
        password (str): contains three pieces of information.
        1. the nubmer of times the letter should be shown
        2. the letter itself
        3. the password

    Returns:
        bool: True if password is valid
              False if password is invalid
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

def count_valid_passwords(file):
    with open(file,"r") as passwords: 

        valid_passwords = 0

        for password in passwords:
            if is_valid(password):
                valid_passwords += 1
        
        return valid_passwords

        
if __name__ == "__main__":
    
    print("ANSWER TO PART ONE:", count_valid_passwords("passwords.csv"))

""" 
PART TWO:
---------

While it appears you validated the passwords correctly, they don't seem to be 
what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password 
policy rules from his old job at the sled rental place down the street! The Official 
Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first 
character, 2 means the second character, and so on. (Be careful; Toboggan Corporate 
Policies have no concept of "index zero"!) Exactly one of these positions must contain 
the given letter. Other occurrences of the letter are irrelevant for the purposes of 
policy enforcement.

Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?
"""

def split_input(input: str):
    
    parts = input.split()

    letter = parts[1][0]
    password = parts[2]

    ranges = parts[0].split("-")
    pos_one = int(ranges[0])
    pos_two = int(ranges[1])

    return pos_one, pos_two, letter, password


def is_valid(password: str) -> bool:

    pos_one, pos_two, letter, password = split_input(password)

    one = password[pos_one - 1] == letter
    two = password[pos_two  - 1] == letter

    if one and two:
        return False
    if not one and not two:
        return False
    return True
    

def count_valid_passwords(file):
    with open(file,"r") as passwords: 

        valid_passwords = 0

        for password in passwords:
            if is_valid(password):
                valid_passwords += 1
        
        return valid_passwords

        
if __name__ == "__main__":
    
    print("ANSWER TO PART TWO:", count_valid_passwords("passwords.csv"))
