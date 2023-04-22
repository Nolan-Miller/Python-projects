# This is a very simple program. I decided to make it after playing the Spelling Bee game on
# the New York Times website. The game has seven letters, with one in the middle. The objective
# is to make as many words as possible with any number of the letters but always including the
# center word. This program takes all the letters on the board as input and checks if a set
# containing all of those words is a subset of any words in the dictionary text file.

# This function returns a list containing all the letters entered by the user
def get_letters():
    return list(input('Enter all letters, with the center one first: '))

def main():
    # The dictionary file should be formatted such that every word has its own line. Each line is stored as\
    # an element in a list
    with open('dictionary.txt', 'r', encoding='utf-8') as f:
        words = [line.strip() for line in f.readlines()]
    res = []
    # Loop until user gives input with the correct amount of unique letters
    while 1:
        letters = get_letters()
        if len(set(letters)) == 7:
            break
    # Store the center word so that it can be used to check if words contain it
    center = letters[0]

    # Check if each word as a set is a subset of valid letters and includes the center letter
    for word in words:
        if set(word).issubset(letters) and center in word:
            res.append(word)

    # Print results
    print('\n'.join(res))

if __name__ == "__main__":
    main()
