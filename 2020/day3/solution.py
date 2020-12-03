def get_map(file):
    with open(file, "r") as map:
        return [list(row)[:-1] for row in map]

def count_trees_in_path(col: int, row: int) -> int:
    x, y = 0, 0
    trees = 0

    while x < len(map):
        if y >= len(map[0]):
            y = y % len(map[0])
        if map[x][y] == "#":
            trees += 1
        x += row
        y += col

    return trees

def find_product_of_trees(slopes: list) -> int:
    
    total_trees = 1

    for slope in listed_slopes:
        total_trees *= count_trees_in_path(slope[0], slope[1])

    return total_trees

if __name__ == "__main__":
    map = get_map("map.csv")
    listed_slopes = [[1,1], [3, 1], [5, 1], [7, 1], [1, 2]]
    print(find_product_of_trees(listed_slopes))