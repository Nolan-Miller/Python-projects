import time

def main():
    p1 = p2 = 0
    line = None
    p1Buff = []
    p2Buff = []

    with open("./input.txt") as f:
        for line in f:
            line = line.strip()

    for i, c in enumerate(line):
        p1Buff.append(c)
        p2Buff.append(c)

        if i >= 3:
            if not p1 and len(set(p1Buff)) == 4:
                p1 = i + 1

            p1Buff.pop(0)

        if i >= 13:
            if not p2 and len(set(p2Buff)) == 14:
                p2 = i + 1

            p2Buff.pop(0)

        if p1 and p2:
            break

    print(f"p1: {p1}, p2: {p2}")


if __name__ == "__main__":
    st = time.time()
    main()
    et = time.time()
    print(f"\nElapsed time: {et - st}")
