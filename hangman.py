word_list = ['word1', 'apple', 'teemo']
import random

# TODO-1 - Generate Random Word

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2 - Generate as many blanks as letters in the word


# TODO-3 - Ask the player to guess a letter

guess = input("Guess a letter: ").lower()
print(guess)

# TODO-4 - Check

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")