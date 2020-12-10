# acc increases accumulator by amount
# jmp jumps to new instruction relative to itself
# nop no operation - one below it goes next
acc = 0

# add the iteration and the instruction to set.
# if in set, then return what the value of the accumulator is

with open("instructions.txt", "r") as instructions:

ins_list = [instruction for instruction in instructions]

def try_this(change_i=None, change_thing=None):
    
    seen = set()
    i = 0
    while i < len(ins_list):

        ins = ins_list[i]
        if (i, ins) in seen:
            return False, i
        seen.add((i, ins))
        if ins_ list[i][:3] == "acc":
            num = ins_list[i][4:]
            acc += int(num)
            i += 1
        elif ins_list[i][:3] == "jmp":
            num = ins_list[i][4:]
            i += (int(num))
        elif ins_list[i][:3] == "nop":
            i += 1


        
