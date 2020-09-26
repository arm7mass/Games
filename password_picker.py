import random
import string

adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red', 'orange',
              'yellow', 'green', 'blue', 'purple', 'fluffy', 'white', 'proud', 'brave']

nouns = ['apple', 'dinosaur', 'ball', 'toaster',
         'duck', 'goat', 'dragon', 'hummer', 'panda']
print('welcome to Password Picker')

while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)

    password = adjective + noun + str(number) + special_char

    print(f" Your Password is:  {password}")

    response = input(" Would you like another Passowrd? Type y or n ")

    if response == "n":
        break
