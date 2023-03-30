# https://adventofcode.com/2022/day/4

import time

def main():
    engulfs = overlaps = 0
    with open("./input.txt") as f:
        for line in f:
            # Strip and cast each line as ints
            elf1, elf2 = [(int(i), int(j)) for i, j in (line.strip().split(",")[0].split("-"), line.strip().split(",")[1].split("-"))]

            # These next two if statements are nested because if the first condition is met, then the second one doesn't need
            # to be checked. This should save a little bit of time. This may be unnecessary, but I wanted to play around with it.

            # Check if both of one elf's points are between the other elf's points
            if elf1[0] >= elf2[0] and elf1[1] <= elf2[1]:
                engulfs+= 1
            elif elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
                engulfs+= 1
            # Check if either elf's starting point is included between the other elf's start and end points
            if elf1[0] <= elf2[0] <= elf1[1]:
                overlaps+= 1
            elif elf2[0] <= elf1[0] <= elf2[1]:
                overlaps+= 1

    print(f"Number of engulfed pairs: {engulfs}")
    print(f"Number of overlapping pairs: {overlaps}")

if __name__ == "__main__":
    st = time.time()
    main()
    et = time.time()
    print(f"\nElapsed Time: {et - st}")
