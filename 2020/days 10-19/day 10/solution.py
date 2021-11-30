def part_one():
    jolts = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]
    jolts = sorted(jolts)
    jolts.append(jolts[-1] + 3)
    differences = dict()

    prev = 0

    for jolt in jolts:
        difference = jolt - prev
        if difference > 3:
            print("GREATER THAN 3")
        if difference not in differences:
            differences[difference] = 0
        differences[difference] += 1
        prev = jolt

    print("PART ONE ANSWER", differences[3] * differences[1])

