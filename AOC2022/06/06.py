import time

def main():
    with open("./input.txt") as f:
        for line in f:
            line = line.strip()
            line = list(line)
            count = 1
            for i in range(len(line) - 14):
                buff = {line[i], line[i + 1], line[i + 2], line[i + 3], line[i + 4], line[i + 5], 
                        line[i + 6], line[i + 7], line[i + 8], line[i + 9], line[i + 10], line[i + 11],
                        line[i + 12], line[i + 13]}
                if len(buff) == 14:
                    print(count+13)
                    print(buff)
                    break
                count+=1


if __name__ == "__main__":
    st = time.time()
    main()
    et = time.time()
    print(f"\nElapsed Time: {et - st}")
