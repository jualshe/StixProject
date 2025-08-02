from pkg_resources import empty_provider

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

colours = {
    "apple": "red",
    "pear": "green",
    "banana": "yellow",
    123: "pink"
}

#retrieving items from dictionary
# print(programming_dictionary["Function"])

# print(colours[123])

# for key in colours:
#     print(key)

# for key in colours:
#     print(colours[key])

#adding a new items to dictionary
programming_dictionary["Loop"] = "The action of doung something over and over again"
# print(programming_dictionary)

#creating a new dictionary
# empty_dictionary = {}
# empty_dictionary []
# print(empty_dictionary)

#wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# print(colours)