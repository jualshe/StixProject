import random
# generate random words
word_list = ["baboon", "camel", "shark" ]
#randomly choose a word from the list
chosen_word = random.choice(word_list)
print(chosen_word)

display = []
word_length = len(chosen_word)
#TODO-1 -print _ for each letter of the random word
for letter in range (0, word_length):
    display += ["_"]
print(display)

# ask user to guess the letter
guess = input("Guess a letter: ").lower()
#TODO-2 - for each guessed letter reveil in a list

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display [position] = letter
print(display)