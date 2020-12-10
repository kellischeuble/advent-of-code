with open("numbers.txt", "r") as numbers:
    number_list = [int(number.rpartition("\n")[0]) for number in numbers]

def check_if_num_is_sum(nums: list, sum: int) -> bool:
    for i, num1 in enumerate(nums):
        for num2 in nums[i+1:]:
            if num1 + num2 == sum:
                return True
    return False

# i = 0
# while i < len(number_list) - 25:
#     if not check_if_num_is_sum(number_list[i:i+25], number_list[i+25]):
#         invalid = number_list[i+25]
#         print("ANSWER TO PART ONE:", invalid)
#         exit()
#     i += 1

invalid = 144381670


# BRUTE FORCE:

def find_contiguous_numbers_add_up(invalid, nums):
    summed = False
    i = 0
    j = 0
    while not summed:
        cur_sum = 0
        cur_numbers = []
        j = i
        while cur_sum <= invalid:
            if cur_sum == invalid and len(cur_numbers) > 1:
                return cur_numbers
                exit()
            cur_sum += nums[j]
            cur_numbers.append([nums[j]])
            j += 1
        i += 1

print(sorted(find_contiguous_numbers_add_up(invalid, number_list)))
print("ANSWER TO PART TWO:", 5779902 + 14752667)



