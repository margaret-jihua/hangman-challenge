import random

# define the bank of words
words = ['amazing', 'awesome', 'snowwhite', 'chestnut', 'jedi', 'google']

# store the drawing hangman in array
drawing = [
    " ____",
    "|    |",
    "|    O",
    "|   -|-",
    "|    /\\",
    "|",
    "-"
]

# randomly pick a word to be the answer key
key = random.choice(words)

# display the current state of word guessed
display = []
for i in range(0, len(key)):
    display += '_'

# try to see how hangman print out
# for i in drawing:
#     print(i)

print(key, display) # TODO delete 

#Game init
print("~~~~~~~~~~~~~~Hangman Game~~~~~~~~~~~~~~")
print("Guess the word or the man will be HANGED")
print("You have 7 guesses\n", ' '.join(display))

print("Hint: This word has {} letters ".format(len(key)))

guess = input("Guess: ")
if guess in key:
    display[key.index(guess)] = guess
    print(' '.join(display))


# while ()