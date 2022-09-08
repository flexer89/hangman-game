import random
import hangman_art
import hangman_words

print(hangman_art.logo)
print("Welcome to hangman game!")
input("Press a key to start . . .")
hangman_art.clear()

lives = 6
finished_game = False

#Random word pick and generate empty answer box
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
answer = []
for _ in range(word_length):
    answer += "_"

#Main part of game, guessing mechanism
while not finished_game:
  guess = input("Guess a letter: ").lower()
  hangman_art.clear()
  if guess in answer:
    print(f"You've already guessed {guess} letter.")
  
  for pos in range(word_length):
    if guess==chosen_word[pos]:
      answer[pos]=guess
  print(f"{' '.join(answer)}")
  
  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word.")
    lives -= 1
    if lives == 0:
      hangman_art.clear()
      print(f"{' '.join(answer)}")
      print("You lose.")
      print(f"The word is {chosen_word}")
      finished_game = True

  if not "_" in answer:
    hangman_art.clear()
    print(f"{' '.join(answer)}")
    print("You win!")
    finished_game = True
    
  print(hangman_art.stages[lives])
