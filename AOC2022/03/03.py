import time
import string

def main():
    priority_sum = badge_sum = 0
    with open("./input.txt") as bags:
        for bag in bags:
            # Read three lines at a time because part 2 is split into sets of three lines each
            bag1 = bag.strip()
            bag2 = bags.readline().strip()
            bag3 = bags.readline().strip()

            # Add to sum of priorities for each line individually for part 1
            priority_sum+= find_priority(find_common_char(bag1))
            priority_sum+= find_priority(find_common_char(bag2))
            priority_sum+= find_priority(find_common_char(bag3))

            # Add to sum of badge priorities for part 2
            badge_sum+= (find_priority(find_badge(bag1, bag2, bag3)))

    print(f"Item prioritiy sum: {priority_sum}")
    print(f"Badge priority sum: {badge_sum}")

# Finds common character between two halfs of a string split down the middle
def find_common_char(line):
    first = line[:len(line) // 2]
    second = line[len(line) // 2:]
    common_char = ''.join(set(first).intersection(second))
    return common_char

# Returns numerical value 1-26 for character values a-z and 27-52 for A-Z
def find_priority(common_char):
    if common_char.islower():
        return string.ascii_lowercase.index(common_char) + 1
    return string.ascii_uppercase.index(common_char) + 27

# Takes three strings as arguments and returns the common char among them
def find_badge(line1, line2, line3):
    common_char = ''.join(set(line1).intersection(line2).intersection(line3))
    return common_char

if __name__ == "__main__":
    st = time.time()
    main()
    et = time.time()
    print(f"\nElapsed Time: {et - st}")
