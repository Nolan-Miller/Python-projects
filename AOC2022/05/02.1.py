with open("input1.txt", encoding="utf-8") as f:

    stacks = [
            ['G', 'B', 'D', 'C', 'P', 'R'],
            ['G', 'V', 'H'],
            ['P', 'M', 'J', 'D', 'Q', 'S', 'N'],
            ['M', 'N', 'C', 'D', 'G', 'L', 'S', 'P'],
            ['S', 'L', 'F', 'P', 'C', 'N', 'B', 'J'],
            ['S', 'T', 'G', 'V', 'Z', 'D', 'B', 'Q'],
            ['Q', 'T', 'F', 'H', 'M', 'Z', 'B'],
            ['F', 'D', 'B', 'M', 'C'],
            ['G', 'Q', 'C', 'F']
        ]
    for s in stacks:
        s = s.reverse()


    # read all the lines of the file into a variable
    lines = f.readlines()

    instruction_list = []

    for line in lines[10:]:
        instruction = line.split()
        num_crates, from_stack, to_stack = int(instruction[1]), int(instruction[3]), int(instruction[5])
        crates_grabbed = stacks[from_stack - 1][-num_crates:]
        #print("crates grabbed:", crates_grabbed)

        # crates_grabbed.reverse()
        
        for crate in crates_grabbed:
            stacks[to_stack - 1].append(crate)
            stacks[from_stack - 1].reverse()
            stacks[from_stack - 1].remove(crate)
            stacks[from_stack - 1].reverse()
        
        #print("curr stacks", stacks)

print("".join([stack[-1] for stack in stacks]))
