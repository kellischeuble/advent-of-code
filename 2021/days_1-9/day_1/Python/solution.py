with open('2021/days_1-9/day_1/input.txt') as f:
    lines = f.readlines()

def part_one():

    prev = 0
    counter = 0
    for line in lines:
        depth_measurement = int(line)
        if (depth_measurement > prev) and (prev != 0):
            counter += 1
        prev = depth_measurement
                
    return counter


def part_two():
    prev = 0
    counter = 0
    for i in range(2, len(lines)):
        window = int(lines[i]) + int(lines[i-1]) + int(lines[i-2])
        if (window > prev) and (prev != 0):
            counter += 1
        prev = window
                
    return counter

print("part one:", part_one())
print("part two:", part_two())

        

