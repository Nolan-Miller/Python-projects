import time

def main():
    with open("input.txt") as f:
        lines = [row.strip() for row in f.readlines()]
    print(task1(lines))

def task1(lines):
    ROWS = len(lines)
    COLS = len(lines[0])

    edge_count = (ROWS * 2) + ((COLS - 2) * 2)
    total = edge_count

    for row in range(1, ROWS-1):
        for col in range(1, COLS-1):
            tree = lines[row][col]

            left = [lines[row][col-i] for i in range(1, col+1)]
            right = [lines[row][col+i] for i in range(1, COLS-col)]
            up = [lines[row-i][col] for i in range(1, row+1)]
            down = [lines[row+i][col] for i in range(1, ROWS-row)]
            
            if max(left) < tree or max(right) < tree or max(up) < tree or max(down) < tree:
                total+= 1

    return total



if __name__ == "__main__":
    st = time.time()
    main()
    et = time.time()
    print(f"\nELAPSED TIME: {round(et-st, 5)}")

