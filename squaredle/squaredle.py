# This program solves a Squaredle puzzle. Go to squaredle.app to play.
# Here are the rules (also shown on the website):

# Squaredle is played on a 4x4 grid of letters.
# Find words by connecting letters up, down, left, right and diagonally. Longer words are worth more points!
# When your progress bar reaches the first star, letters on the board will show a number — how many words start with that square. Reach the star after that for another new trick!
# Squaredle, like Scrabble, doesn't accept capitalized or hyphenated words.

# This program uses all words longer than 4 letters in the Scrabble dictionary.

import numpy as np

# This function finds all possible words on a board and returns a list of them
# mat is a 2d array that holds all letters on the board
# visited is a set that holds tuples of all letters already used in a word
# i and j are the location of the current letter being added to the word
# curr_word is all the letters in the path checked so far
# words is a list of all Scrabble words
# results is a list of all valid words found so far
def findWords(mat, visited, i, j, curr_word, words, results):
    # Store dimensions of board
    ROWS, COLS = mat.shape
    # Add current letter tile to visited
    visited.add((i, j))
    # Add current letter to the current word to be tested
    curr_word += mat[i][j]
    # If the current word is in the dictionary, add it to results
    if len(curr_word) >= 4 and curr_word in words:
        results.add(curr_word)
    # Check if there are any words if any surrounding letters are appended to current word
    for row in range(i - 1, i + 2):
        for col in range(j - 1, j + 2):
            if 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in visited:
                findWords(mat, visited, row, col, curr_word, words, results)
    # Done checking this letter, remove it from visited
    visited.remove((i, j))
    # Remove letter from current word
    curr_word = curr_word[:-1]

def main():
    # Declare vars and get scrabble dictionary loaded
    words = ""
    results = set()
    visited = set()
    mat = []
    with open("dictionary.txt", encoding="utf-8") as f:
        words = set(f.read().splitlines())

    # Gather input from the user to make the game board and store it in mat
    while len(mat) < 4:
        n = len(mat) + 1
        mat.append(input(f"Enter row #{n}: ").lower())
    mat = np.array([list(mat[i]) for i in range(len(mat))])
    ROWS, COLS = mat.shape

    # Find every possible word that can be made with each letter as a starting point
    for i in range(ROWS):
        for j in range(COLS):
            findWords(mat, visited, i, j, "", words, results)

    # Print results
    print()
    for i in sorted(list(results)):
        print(i)

if __name__ == "__main__":
    main()
