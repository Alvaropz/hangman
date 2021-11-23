import random
import string
import re
from pathlib import Path

def hangman(alphabet_set, word_chosen, attemps, hangman_doll):
    word_list = list(word_chosen)
    returned_s = ["_"]*len(word_list)
    print("Word to guess: " + " ".join(returned_s))
    print("-------------------------------------")
    while attemps < len(hangman_doll)-1:
        input_str = input("Give me a letter!: ")
        if not re.match("^[a-z]*$|^[A-Z]*$", input_str) or len(input_str) != 1:
            print("Error! Only letters a-z, A-Z allowed! And only one letter at most.")
        elif input_str.lower() in alphabet_set:
            print("You already said the letter '{}'. Don't be cheecky.".format(input_str))
        else:
            input_str = input_str.lower()
            if input_str in word_list:
                print("That's right!")
                for i, char in enumerate(word_list):
                    if char == input_str:
                        returned_s[i] = char
                if not "_" in returned_s:
                    return print("You guessed it! The word was '{}'.".format(word_chosen.upper()))
            else:
                print("The letter '{}' is not in the chosen word!".format(input_str))
                print(hangman_doll[attemps])
                attemps += 1
            alphabet_set.add(input_str)
            print("Letters you have said so far: {}.".format(", ".join(sorted(alphabet_set))))
            print("Word to guess: " + " ".join(returned_s).strip().upper())
            print("-------------------------------------")
    print(hangman_doll[attemps])
    return print("Oh no! You didn't guess the word... The word was '{}'. Best luck next time!".format(word_chosen.upper()))
    
alphabet_set = set()
hangman_doll = ["""
                ---------
                |       |
                |
                |
                |
                |
                |
                -
                """,
                """
                ---------
                |       |
                |       O
                |
                |
                |
                |
                -
                """,
                """
                ---------
                |       |
                |       O
                |       |
                |
                |
                |
                -
                """,
                """
                ---------
                |       |
                |       O
                |      \\|
                |
                |
                |
                -
                """,

                """
                ---------
                |       |
                |       O
                |      \\|/
                |
                |
                |
                -
                """,
                """
                ---------
                |       |
                |       O
                |      \\|/
                |       |
                |
                |
                -
                """,
                """
                ---------
                |       |
                |       O
                |      \\|/
                |       |
                |      /
                |
                -
                """,
                """
                ---------
                |       |
                |       O
                |      \\|/
                |       |
                |      / \\
                |
                -
                """,
]
attemps = 0
path_file = Path(__file__).resolve().parent
with open(str(path_file) + "\hangman.txt", 'r') as list_of_words:
    word_chosen = random.choice(list(list_of_words)).rstrip()

hangman(alphabet_set, word_chosen, attemps, hangman_doll)

