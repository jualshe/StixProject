import random
# generate random words
word_list = ["baboon", "camel", "shark" ]
#randomly choose a word from the list
chosen_word = random.choice(word_list)
print(chosen_word)

display = []
word_length = len(chosen_word)

for letter in range (0, word_length):
    display += ["_"]
print(display)

#TODO-1 - Use a while loop to let the user guess again.
# Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word.
# At that point display has no more blanks ("_"). Then you can tell the user they've won

while "_" in display:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display [position] = letter
    print(display)