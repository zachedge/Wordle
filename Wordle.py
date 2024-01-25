# # File: Wordle.py

# """
# This module is the starter file for the Wordle assignment.
# BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
# """

# import random

# from WordleDictionary import FIVE_LETTER_WORDS
# from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

# def wordle():

#     def enter_action(s):
#         if is_legitimate_word(s):
#             gw.show_message("Congratulations! You entered a legitimate word.")
#         else:
#             gw.show_message("Not in word list")

#     def is_legitimate_word(word):
#         return word.upper() in map(str.upper, FIVE_LETTER_WORDS)


#     gw = WordleGWindow()
#     gw.add_enter_listener(enter_action)

#     # Pick a random word from the FIVE_LETTER_WORDS list
#     solution_word = random.choice(FIVE_LETTER_WORDS)

#     # Display the random word in the first row of boxes
#     for col in range(N_COLS):
#         gw.set_square_letter(0, col, solution_word[col])

# # Startup code

# if __name__ == "__main__":
#     wordle()

# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR

def wordle():

    def enter_action(s):
        s = s.upper()  # Convert the guessed word to uppercase
        if is_legitimate_word(s):
            update_colors(s)
            check_solution()
        else:
            gw.show_message("Not in word list")

    def is_legitimate_word(word):
        return word in [w.upper() for w in FIVE_LETTER_WORDS]

    def update_colors(word):
        for col in range(N_COLS):
            guessed_letter = word[col]
            correct_letter = solution_word[col]

            if guessed_letter == correct_letter:
                gw.set_square_color(gw.get_current_row(), col, CORRECT_COLOR)
            elif guessed_letter in solution_word:
                gw.set_square_color(gw.get_current_row(), col, "yellow")
            else:
                gw.set_square_color(gw.get_current_row(), col, "gray")

    def check_solution():
        if all(gw.get_square_color(gw.get_current_row(), col) == CORRECT_COLOR for col in range(N_COLS)):
            gw.show_message("Congratulations! You guessed the word.", color="green")
            new_word()
        else:
            gw.show_message("Try again.")
            gw.set_current_row(gw.get_current_row() + 1)

    def new_word():
        nonlocal solution_word
        solution_word = random.choice(FIVE_LETTER_WORDS)
        solution_word = solution_word.upper()  # Convert the solution word to uppercase
        gw.set_current_row(0)
        for col in range(N_COLS):
            gw.set_square_letter(0, col, " ")  # Hide the solution word
            gw.set_square_color(0, col, "unknown")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Pick a random word from the FIVE_LETTER_WORDS list
    solution_word = random.choice(FIVE_LETTER_WORDS)
    solution_word = solution_word.upper()  # Convert the solution word to uppercase

    # Display the random word in the corner for debugging
    debug_text = "Debug: " + solution_word
    gw.show_message(debug_text, color="gray")

# Startup code

if __name__ == "__main__":
    wordle()
