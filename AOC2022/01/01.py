import time

def pop_max(cals):
    max_val = max(cals)
    cals.remove(max(cals))
    return max_val

def load_list(f, cals):
    cur = 0
    for line in f:
        if line == "\n":
            cur = 0
        else:
            cur+= int(line)
        cals.append(cur)

def main():
    f = open("./input.txt")
    cals = []

    load_list(f, cals)

    first = pop_max(cals)
    second = pop_max(cals)
    third = pop_max(cals)
    total = first + second + third

    print(f"Largest value = {first}")
    print(f"Sum of three largest values = {total}")

if __name__ == "__main__":
    st = time.time()
    main()
    et = time.time()
    elapsed = et - st
    print(f"Elapsed time: {elapsed}")
