# Hangman Challenge

This is the classic hangman game built in Python. In hangman, a secret word is chosen and the user tries to guess each letter. Each correct guess reveals all instances of that letter. Each incorrect guess draws another body part on the poor guy getting hanged. The user wins if they reveal the entire word. They lose if the whole person is drawn on the noose.

## Functionality

* Store a list (or tuple) of 5 to 10 words in the script.
* Randomly choose a word from this list as the secret word.
* Display the unrevealed word as underscores (with the same length.)
* Prompt the user to enter a letter.
* If the letter is in the word, mark it as revealed and visually display that letter in the word.
* If the letter is incorrect, draw another part onto the stick person.

### Pseudocode

1. Initialize the game: Initialize all variables to default values.
2. Display hangman or number of guesses remaining.
3. Randomly select a secret word.
4. Display the word as blanks.
5. Display the letters guessed so far.
6. Ask the user for a letter.
7. Determine if letter is correct or incorrect.
8. If incorrect, add the letter to the guessed list, decrement remaining guesses, and/or draw another bit of the hangman.
9. If correct, add the letter to the guessed list, redraw the secret word with the new letter(s) showing.
10. Loop back up to step 6 and continue until the word is fully revealed or guesses are used up.

### Drawing hangman

I store the drawing line by line in an array and print it out from bottom to top, so taht users can have up to 7 wrong guesses:

```
 ____
|    |
|    O
|   -|-
|    /\
|
-
```

## Game Start

```
~~~~~~~~~~~~~~Hangman Game~~~~~~~~~~~~~~
Guess the word or the man will be HANGED
You can have up to 7 wrong guesses

Hint: This word has 4 letters  _ _ _ _

Guess: 
```

Users can guess one letter each time, if they enter multiple letters they will get warming and enter again

```
Guess: ds
One Letter At A Time!

Guess: 
```

## Game Status

As the game goes, users can see the hangman drawing step by step if they guess wrong, and letter reveals if they guess correct 

```
Guess: g
Wrong Guess❌
👀 Current Guesses: _ _ _ _
😿 Hangman Status:
|
-

Guess: h
Wrong Guess❌
👀 Current Guesses: _ _ _ _
😿 Hangman Status:
|    /\
|
-

Guess: r
Wrong Guess❌
👀 Current Guesses: _ _ _ _
😿 Hangman Status:
|   -|-
|    /\
|
-

Guess: d
Success revealed one letter 'd'✅
👀 Current Guesses: _ _ d _
😿 Hangman Status:
|   -|-
|    /\
|
-

Guess: j
Success revealed one letter 'j'✅
👀 Current Guesses: j _ d _
😿 Hangman Status:
|   -|-
|    /\
|
-

Guess: x
Wrong Guess❌
👀 Current Guesses: j _ d _
😿 Hangman Status:
|    O
|   -|-
|    /\
|
-

Guess:
```

## Gameover

If the user wins:
```
Guess: i
Success revealed one letter 'i'✅
👀 Current Guesses: j e d i
😿 Hangman Status:
|    O
|   -|-
|    /\
|
-
You saved the hanging man🙏

Do you want to play again? 'yes' or 'no'
```

if the user loses:
```
Guess: g
Wrong Guess❌
👀 Current Guesses: g _ _ g _ _
😿 Hangman Status:
 ____
|    |
|    O
|   -|-
|    /\
|
-
HANGED THE MAN💀

Do you want to play again? 'yes' or 'no'
```

## Game Loop

Users will be asked if they want to play again, they can enter yes/no to restart/end the game. If they enter something else, they will be asked to re-enter

```
Do you want to play again? 'yes' or 'no'
t
I am not sure what you mean, please only enter 'yes' or 'no'

Do you want to play again? 'yes' or 'no'
3
I am not sure what you mean, please only enter 'yes' or 'no'

Do you want to play again? 'yes' or 'no'
gsdfg
I am not sure what you mean, please only enter 'yes' or 'no'

Do you want to play again? 'yes' or 'no'
```

Game Restart:
```
Do you want to play again? 'yes' or 'no'
y
~~~~~~~~~~~~~~Hangman Game~~~~~~~~~~~~~~
Guess the word or the man will be HANGED
You can have up to 7 wrong guesses

Hint: This word has 7 letters  _ _ _ _ _ _ _

Guess:
```

EndGame:
```
Do you want to play again? 'yes' or 'no'
n
Thank you for playing
```
