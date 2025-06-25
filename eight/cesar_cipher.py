# def greet_with_name(name):
#     print(f"AA " + name)
#     print(f"BB " + name)
#     print(f"CC " + name)
#
# greet_with_name("Brownie")
#
#
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"what is it like in  {location}?")
# greet_with("Julia", "Lviv")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
