import random
# generate random words
word_list = ["baboon", "camel", "shark" ]

#TODO1 - randomly choose a word from the list
choosen_word = random.choice(word_list)
print(choosen_word)

#TODO2 -  ask user to guess the letter
guess_letter = input("enter letter: ")
print(guess_letter)

#TODO3 - check is the letter is in the word
if guess_letter in choosen_word:
    print("HOORAHH!")
else:
    print("NOOOAAAAWWWW!")


#TODOS:
#generate blanks for the letters