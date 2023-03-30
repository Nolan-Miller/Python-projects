import time

def main():
    with open("./input2.txt") as f:
        # Create stacks
        stacks = create_stacks(f)
        for stack in stacks:
            stack = stack.reverse()
        f.readline()
        parse_movements(f, stacks)
        top_of_stacks = ""
        for s in stacks:
            top_of_stacks+= (s[-1])
        print(f"Part 1: {top_of_stacks.strip()}")

    with open("./input2.txt") as f:
        stacks = create_stacks(f)
        for stack in stacks:
            stack = stack.reverse()
        f.readline()
        for s in stacks:
            print(s)
        parse_movements2(f, stacks)
        '''
        top_of_stacks = ""
        for s in stacks:
            top_of_stacks+= (s[-1])
        print(f"Part 2: {top_of_stacks.strip()}")
        '''
        

def parse_movements2(f, stacks):
    for line in f:
        if "move" in line:
            nums = [int(s) for s in line.split() if s.isdigit()]
        print()
        moved_vals = stacks[nums[1] - 1][len(stacks[nums[1] - 1]) - nums[0]:]
        src = stacks[nums[1] - 1].pop(-1)
        for v in moved_vals:
            stacks[nums[2] - 1].append(v)
        print(f"MOVING {moved_vals} FROM {nums[1]} TO {nums[2]}")

def parse_movements(f, stacks):
    for line in f:
        if "move" in line:
            nums = [int(s) for s in line.split() if s.isdigit()]
        for i in range(1, nums[0]+1):
            stacks[nums[2] - 1].append(stacks[nums[1] - 1].pop(-1))
     
def create_stacks(f):
    stacks = []
    for line in f:
        if "[" in line:
            continue
        num_stacks = int(line.strip()[-1])
        break
    for i in range(1, num_stacks+1):
        stacks.append([])
    # Move pointer back to start of file
    f.seek(0)
    for line in f:
        if "move" in line or "[" not in line or line == "\n":
            break
        i = 1
        vals = ""
        while i <= len(line):
            vals+= (line[i])
            i+= 4
        i = 0
        for char in vals:
            if char != " ":
                stacks[i].append(char)
            i+= 1
    return stacks

if __name__ == "__main__":
    st = time.time()
    main()
    et = time.time()
    print(f"\nElapsed time: {et - st}")
