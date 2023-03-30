import time

def main():
    total_score1 = total_score2 = 0
    with open("./input.txt") as f:
        for line in f:
            opp, player = line.split(" ")
            opp = opp.strip()
            player = player.strip()
            total_score1+= get_score(opp, player)
            total_score2+= get_result(opp, player)
        print(f"Part 1: {total_score1}")
        print(f"Part 2: {total_score2}")

def get_result(opp, player):
    round_score = 0
    if opp == "A": # ROCK
        if player =="X":
            round_score = 3
        if player == "Y":
            round_score = 4
        if player == "Z":
            round_score = 8

    if opp == "B": # PAPER
        if player == "X":
            round_score = 1
        if player == "Y":
            round_score = 5
        if player == "Z":
            round_score = 9

    if opp == "C": #SCISSORS
        if player == "X":
            round_score = 2
        if player == "Y":
            round_score = 6
        if player == "Z":
            round_score = 7

    return round_score

def get_score(opp, player):
    round_score = 0

    if player == "X":
        round_score+= 1
        if opp == "A":
            round_score += 3
        elif opp == "B":
            round_score += 0
        elif opp == "C":
            round_score += 6

    elif player == "Y":
        round_score+= 2
        if opp == "A":
            round_score += 6
        elif opp == "B":
            round_score += 3
        elif opp == "C":
            round_score += 0

    elif player == "Z":
        round_score+= 3
        if opp == "A":
            round_score += 0
        elif opp == "B":
            round_score += 6
        elif opp == "C":
            round_score += 3

    return round_score

if __name__ == "__main__":
    st = time.time()
    main()
    et = time.time()
    print(f"\nELAPSED TIME: {et - st}")
