f = open("./sample.txt").read().strip()
lines = [x for x in f.split("\n")]

pwd = ""
dirs = {}

for line in lines:
    if line.strip() == "":
        continue
    if line[0] == "$":
        _, command, *args = line.split()
        if command == "cd":
            print(args)

