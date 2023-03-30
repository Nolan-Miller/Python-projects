moves = open('input.txt', 'r').read().splitlines()

def test(moves, withAim = False):
    if withAim:
        horiz = 0
        depth = 0
        aim = 0
        for move in moves:
            direction, incr = move.split(" ")
            if direction == "forward":
                horiz += int(incr)
                depth += int(incr) * aim
            elif direction == "down":
                aim += int(incr)
            elif direction == "up":
                aim -= int(incr)
    else:
        horiz = 0
        depth = 0
        for move in moves:
            direction, incr = move.split(' ')
            if direction == 'forward':
                horiz += int(incr)
            if direction == 'down':
                depth += int(incr)
            if direction == 'up':
                depth -= int(incr)
    return horiz * depth

print(f'Part 1: {test(moves)}')
print(f'Part 2: {test(moves, True)}')
