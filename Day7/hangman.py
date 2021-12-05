# HANGMAN

import random
import hangmanart
import hangmanwords

print(hangmanart.title_art)
print("----------WELCOME TO HANGMAN GAME---------")

word_list = hangmanwords.hangman_words
life_art = hangmanart.Hangman_Pics
life_art_index = 0

chosen_word_index = random.randint(0, len(word_list) - 1)

chosen_word = word_list[chosen_word_index]

lives = 6

display = []

for i in chosen_word:
    display.append("_")

flag = False

while not flag:
    guess = input("Enter a letter ").lower()
    count = 0

    # check if the letter is in the word and also set the values of display
    for letter in range(len(chosen_word)):
        if guess == chosen_word[letter]:
            # letter matches
            display[letter] = chosen_word[letter]
            count += 1

    if count == 0:
        lives -= 1
        print(f"Oops! the letter {guess} is not in the word . You loose a life")
        print(hangmanart.Hangman_Pics[life_art_index])
        life_art_index += 1

    # check if all the letters has been filled then come out of the loop else run the loop
    if '_' in display:
        flag = False
    else:
        flag = True

    # check for lives
    if lives == 0:
        flag = True

    print(display)
    print(f"lives = {lives}")

if lives == 0:
    print("You Lose")
else:
    print("You Win")
