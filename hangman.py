import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["baboon", "camel", "shark" ]

chosen_word = random.choice(word_list)
print(chosen_word)

display = []
word_length = len(chosen_word)

for letter in range (0, word_length):
    display += ["_"]
print(display)

end_of_the_game = False

lives = 6

while not end_of_the_game:
    guess = input("Guess a letter: ").lower()
    lives: object


    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display [position] = letter
    if guess not in chosen_word:
            lives -=1
            print(f"lives: {lives}")
            print(stages[lives])
    print(display)

    if not "_" in display:
        end_of_the_game = True
        print("You won!")
    if lives == 0:
        end_of_the_game = True
        print("You loose!")
