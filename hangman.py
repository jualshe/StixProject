import random
from hangman_art import  logo, stages
from hangman_words import word_list

print(logo)
display = []

chosen_word = random.choice(word_list)
print(chosen_word)

word_length = len(chosen_word)
for letter in range (0, word_length):
    display += ["_"]
print(display)

end_of_the_game = False
lives = 6
wrong_guesses = []

while not end_of_the_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've chosen {guess}. And you've already guessed {guess}.")

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display [position] = letter
    print(display)

    if guess in wrong_guesses:
        print(f"You've chosen {guess}. And you've already guessed {guess}. It's not in the list!")
    elif guess not in chosen_word:
        wrong_guesses += guess
        lives -=1
        print(f"You guessed '{guess}' that's not in the word. You lose a life.")
        if lives == 0:
            end_of_the_game = True
            print("You lose!")
        print(f"lives: {lives}")
        print(stages[lives])

    if not "_" in display:
        end_of_the_game = True
        print("You won!")