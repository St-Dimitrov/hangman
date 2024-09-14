word_list = ['word1', 'apple', 'teemo']
import random

# TODO-1 - Generate Random Word

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2 - Generate as many blanks as letters in the word
placeholder = ""
word_lenght = len(chosen_word)
print(word_lenght)
for position in range(word_lenght):
    placeholder += "_"
print(placeholder)

# TODO-3 - Ask the player to guess a letter

game_over = False
lives = 5
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    print(guess)
 

# TODO-4 - Check
    print(lives)
    display = ""

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose.")

    for letter in chosen_word:
        if letter == guess:
            correct_letters.append(letter)
            display += letter
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        print("You win.")
        game_over = True