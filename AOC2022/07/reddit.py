import time

def main():
    with open("./input.txt") as f:
        res1 = limit = 0
        res2 = 1000000000
        sizes = dict()
        paths = set()
        pwd = tuple()

        for line in f:
            line = line.strip()
            if line in ["$ cd /", "$ ls"] or not line or line == "$ cd ..":
                if line == "$ cd ..":
                    pwd = pwd[:-1]
                continue
            if line.startswith('$ cd '):
                pwd = (*pwd, line.split(" ")[2])
                continue
            size, name = line.split(" ") #line.split(" ")[0], line.split(" ")[1]
            if "dir" == size:
                paths.add((*pwd, name,)) 
            else:
                sizes[(*pwd, name,)] = int(size)

        for size in sizes.values():
            limit+= size
        limit -= 40000000

        dir_sizes = { 
            dir_path: sum(
                size for key, size in sizes.items() if 
                    tuple_to_path(dir_path) in tuple_to_path(key)
            ) for dir_path in paths 
        }

        for d in dir_sizes.values():
            if d <= 100000:
                res1+= d
            if limit < d:
                res2 = min(res2, d)

        print(f"Part 1: {res1}")
        print(f"Part 2: {res2}")

def tuple_to_path(tup):
    result = ""
    for t in tup:
        result+= t + "/"
    return result

if __name__ == "__main__":
    st = time.time()
    main()
    et = time.time()
    print(f"\nElapsed time: {et - st}")
