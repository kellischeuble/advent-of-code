import math

START = 1
ROWS = 128
COLUMNS = 8


def get_seat_placemet(characters: str) -> tuple:
    """
    Args:
        characters (str): string of characters specifying
        the location of the seat through binary space 
        partitioning. The first 7 characters are front/back,
        the last 3 characters are left/right.

    Returns:
        tuple: row coordinate location for seat
    """

    rows = characters[:7]
    cols = characters[7:]

    def binary_search(chars: str, position_lower: int, position_upper: int) -> int:
        """
        Recursion to find the location of either the row or the column 
        (Direction for rows vs. cols must be calculated separately)

        Args:
            chars (str): directions for rows or columns
            position_lower (int): current lowest possible seat row/col
            position_upper (int): current hightest possible seat row/col

        Returns:
            int: the row or col of the seat
        """

        if len(chars) == 1:
            if chars == "B" or chars == "R":
                return position_upper
            else:
                return position_lower
        char = chars[0]
        if char == "B" or char == "R":
            position_lower = math.ceil((position_upper + position_lower) / 2)
        else:
            position_upper = math.floor((position_upper + position_lower) / 2)
        chars = chars[1:]
        return binary_search(chars, position_lower, position_upper)

    return (binary_search(rows, START, ROWS) - 1), (
        binary_search(cols, START, COLUMNS) - 1
    )


def get_seat_id(row: int, col: int) -> int:
    """
    Finds the seat ID given the seat coordinates given the rules:
    multiply the row by 8, then add the column

    Args:
        row (int): row of the seat
        col (int): column of the seat

    Returns:
        int: unique seat ID
    """
    return (row * 8) + col


def get_all_seat_codes(file: str) -> list:
    """
    Parses file and calculates the seat code for
    each individual seat. 
    #TODO: store in BST instead of a list

    Args:
        file (str): file name

    Returns:
        list: sorted list of all seat codes
    """

    seat_codes = []

    with open(file, "r") as seats:
        for seat in seats:
            row, col = get_seat_placemet(seat)
            seat_id = get_seat_id(row, col)
            seat_codes.append(seat_id)

    return sorted(seat_codes)


def find_missing_seat(seat_codes: list) -> int:
    """
    Iterates through list of seat codes and finds
    The missing seat. There are some missing seats in
    the front/back of plane, but the rules say that our
    seat is in the middle of two taken seats.

    Args:
        seat_codes (list): sorted list of all seat coes

    Returns:
        int: missing seat code
    """
    set_seats = set(seat_codes)

    lower = seat_codes[0]
    upper = seat_codes[-1]

    while not lower == upper:
        if (
            (lower not in set_seats)
            and (lower - 1 in set_seats)
            and (lower + 1 in set_seats)
        ):
            return lower
        lower += 1


if __name__ == "__main__":
    seat_codes = get_all_seat_codes("seats.csv")
    seat = find_missing_seat(seat_codes)
    print("ANSWER TO PART ONE: ", seat_codes[-1])
    print("ANSWER TO PART TWO: ", seat)
