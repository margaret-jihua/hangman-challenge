import random

# define the bank of words
words = ['amazing', 'awesome', 'snowwhite', 'chestnut', 'jedi', 'google', 'banana', 'python', 'nutella']

# define global variable
# key = ''
# display = []
# hangman = []

# initialize the game
def game_init():
    global key, display, hangman, drawing

    display = []
    hangman = []

    # randomly pick a word to be the answer key
    key = random.choice(words)

    # display the current state of word guessed
    for i in range(0, len(key)):
        display += '_'
    
    # define the hangman drawing in array
    drawing = [
        " ____",
        "|    |",
        "|    O",
        "|   -|-",
        "|    /\\",
        "|",
        "-"
    ]


# check if the letter user input is in the answer key
def game_guess():
    global key, display, hangman, drawing

    guess = input("\nGuess: ")
    if len(guess) != 1: # prevent multiple input
        print("One Letter At A Time!")
        game_guess()
    else:
        if guess in key:
            display[key.index(guess)] = guess
            # replace this letter in key with '#'
            # if there are duplicate letters in the answer key, replace first one 
            key = key.replace(guess, '#', 1)
            print("Success revealed one letter '{}'✅".format(guess))
        else:
            hangman.insert(0, drawing.pop())
            print("Wrong Guess❌")


def game_run():
    game_init()
    print(key) # TODO delete
    print("~~~~~~~~~~~~~~Hangman Game~~~~~~~~~~~~~~")
    print("Guess the word or the man will be HANGED")
    print("You can have up to 7 wrong guesses\n")
    print("Hint: This word has {} letters ".format(len(key)), ' '.join(display))
    answer = key
    while answer != ''.join(display):
        game_guess()
        print("👀 Current Guesses: {}".format(' '.join(display)))
        if hangman != []:
            print("😿 Hangman Status:")
            for i in hangman:
                print(i)       
        if drawing == []:
            print("HANGED THE MAN💀")
            break
    else:
        print('You saved the hanging man🙏')

game_run()
while(True):
    game_continue = input("\nDo you want to play again? 'yes' or 'no'\n")
    if game_continue == 'yes' or game_continue == 'y':
        game_run()
    elif game_continue == 'no' or game_continue == 'n':
        print("Thank you for playing")
        break
    else:
        print("I am not sure what you mean, please only enter 'yes' or 'no'")