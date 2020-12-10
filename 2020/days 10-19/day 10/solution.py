differences = {}

with open("jolts.txt", "r") as jolts:
    jolts = sorted([int(jolt.rpartition("\n")[0]) for jolt in jolts])
    prev = 0

    # add built-in joltage adapter
    jolts.append(jolts[-1] + 3)

    for jolt in jolts:
        difference = abs(prev - jolt)
        if not difference in differences:
            differences[difference] = 0
        differences[difference] += 1
        prev = jolt

    print("ANSWER TO PART ONE:", differences[1] * differences[3])


