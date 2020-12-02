"""
PART ONE:
---------
Before you leave, the Elves in accounting just need you to fix your expense report 
(your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then 
multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying 
them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 
2020; what do you get if you multiply them together?
"""

import csv

def find_entries(expense_report: list):
    """
    Takes the list of expense reports and returns the two 
    entries that sum up to 2020

    Args:
        expense_report (list): 

    Returns:
        num1, num2 (ints): two entries that add up to 2020
    """

    seen = set()

    for entry in expense_report:
        # cast to int because they are stored as strings in 
        # expense_report
        entry = int(entry)
        difference = 2020 - entry
        if difference in seen:
            return entry, difference
        else:
            seen.add(entry)

def multiply_entries(entry_one: int, entry_two:int) -> int:
    return entry_one * entry_two

if __name__ == "__main__":

    with open("expense_report.csv","r") as report: 
        entry_one, entry_two = find_entries(report)
        print("ANSWER PART ONE:", multiply_entries(entry_one, entry_two))

""" 
PART TWO:
---------

The Elves in accounting are thankful for your help; one of them even offers you a 
starfish coin they had left over from a past vacation. They offer you a second one 
if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 
675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
"""

def find_entries(expense_report: list):

    seen = set()

    for entry_one in expense_report:
        entry_one = int(entry_one)
        for entry_two in seen:
            difference = 2020 - (entry_one + entry_two)
            if difference in seen:
                return entry_one, entry_two, difference
        seen.add(entry_one)

def multiply_entries(entry_one: int, entry_two:int, entry_three: int) -> int:
    return entry_one * entry_two * entry_three

if __name__ == "__main__":

    with open("expense_report.csv","r") as report: 
        entry_one, entry_two, entry_three = find_entries(report)
        print("ANSWER PART TWO:", multiply_entries(entry_one, entry_two, entry_three))