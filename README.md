## Hangman game

# Description

Hangman is a simple and popular game

User has to guess letters of randomly picked word.
The word to guess is represented by a row of dashes representing each letter of the word.
If player suggests a letter which occurs in the word, it is written in all its correct positions. If the suggested letter does not occur in the word, one element of a hanged stick figure is drew.


# Example Input

```
 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    


Welcome to hangman game!
Press a key to start . . .
```

# Example Output

```
m a t r i x
You win!

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
```

```
v _ _ _ _
You lose.
The word is vixen

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
```

# Reference
Explanation of how console clearing is working
[https://stackoverflow.com/a/50560686]