with open('2021/days_1-9/day_2/input.txt') as f:
    lines = f.readlines()

def part_one():

    horizontal_position = 0
    depth = 0

    for line in lines:

        direction = line[0]
        position = int(line[-2])

        if direction == 'u':
            depth -= position
        if direction == 'd':
            depth += position
        if direction == 'f':
            horizontal_position += position

    return horizontal_position * depth


def part_two():

    horizontal_position = 0
    depth = 0
    aim = 0

    for line in lines:

        direction = line[0]
        position = int(line[-2])

        if direction == 'u':
            aim -= position
        elif direction == 'd':
            aim += position
        if direction == 'f':
            horizontal_position += position
            depth += (aim * position)

    return horizontal_position * depth

print("part one:", part_one())
print("part two:", part_two())
