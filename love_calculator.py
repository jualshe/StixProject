print("The Love Calculator is calculating your score...")
name1 = input("What is your name?")
name2 = input("What is their name?")

combined_names = name1 + name2

names = combined_names.lower()
one = names.count("t" and "r" and "u" and "e")
two = names.count("l" and "o" and "v" and "e")

result = str(one)+ str(two)
print(f"your result is {result}")




# TRUE
# LOVE
# %
#
# For Love Scores less than 10 or greater than 90, the message should be:
#
# "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
#
# "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:
#
# "Your score is *z*."