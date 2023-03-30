import time

# How to find top three values in one line
def top_three_sum(cals):
    return (f"Sum of three largest entries: {sum(sorted(cals, reverse=True)[:3])}")

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
    print(f"Largest value stored: {max(cals)}")
    print(f"Sum of top three largest values: {top_three_sum(cals)}")

if __name__ == "__main__":
    st = time.time()
    main()
    et = time.time()
    elapsed = et - st
    print(f"Elapsed time: {elapsed}")
