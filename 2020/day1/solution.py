import csv

def find_entries_part_one(expense_report: list) -> tuple:

    seen = set()

    for entry in expense_report:
        entry = int(entry)
        difference = 2020 - entry
        if difference in seen:
            return entry * difference
        else:
            seen.add(entry)

    raise ValueError("Not Found")

def find_entries_part_two(expense_report: list) -> tuple:

    seen = set()

    for entry_one in expense_report:
        entry_one = int(entry_one)
        for entry_two in seen:
            difference = 2020 - (entry_one + entry_two)
            if difference in seen:
                return entry_one * entry_two * difference
        seen.add(entry_one)

    raise ValueError("Not Found")

def solve_part_one():
    with open("expense_report.csv","r") as report: 
        print("ANSWER PART ONE:", find_entries_part_one(report))

def solve_part_two():
    with open("expense_report.csv","r") as report: 
        print("ANSWER PART ONE:", find_entries_part_two(report))

if __name__ == "__main__":
    solve_part_one()
    solve_part_two()