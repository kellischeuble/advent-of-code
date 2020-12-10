def get_map(file: str) -> list:
    """
    Returns a 2D list containing the map from file
    Takes out the last newline char in each row
    """
    with open(file, "r") as MAP:
        return [list(row)[:-1] for row in MAP]


def count_trees_in_path(right: int, down: int) -> int:
    """
    Counts the number of trees that one would encounter
    in the map. The map repeats infinitely with the same pattern 
    to the right

    Args:
        right (int): number of slopes to move right
        down (int): number of slopes to move left

    Returns:
        int: the number of trees encountered
    """
    row, col = 0, 0
    trees = 0

    while row < len(MAP):
        if col >= len(MAP[0]):
            col = col % len(MAP[0])
        if MAP[row][col] == "#":
            trees += 1
        row += down
        col += right

    return trees


def find_product_of_trees(slopes: list) -> int:
    """
    Looks at all paths taken and finds the number
    of trees encountered in each one, then multiplies
    all of those numbers together

    Args:
        slopes (list): list of all of the slopes with 
                        desired paths

    Returns:
        int: product of trees encountered in all paths
    """
    prod_trees_encountered = 1

    for right, down in LISTED_SLOPES:
        prod_trees_encountered *= count_trees_in_path(right, down)

    return prod_trees_encountered


if __name__ == "__main__":
    MAP = get_map("map.csv")
    LISTED_SLOPES = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    print(find_product_of_trees(LISTED_SLOPES))
