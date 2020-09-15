#imports wordlist.py
import wordlist

#gets the word from wordlist.py at random
def get_word():
    word=wordlist.get_random_word()
    return word.upper()

#adds spaces to the word obtained from wordlist.py
def add_spaces(word):
    word_with_spaces=" ".join(word)
    return word_with_spaces

#draws the screen that shows the number of guesses, number of incorrect guesses, current guessed letters, and the current word
def draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word):
    print("-"*79)
    print("Word:", add_spaces(displayed_word), "Guesses:", num_guesses,
          "Wrong:", num_wrong,
          "Tried:", add_spaces(guessed_letters))

#allows the user to input just one letter
def get_letter(guessed_letters):
    while True:
        guess=input("Enter a letter: ").strip().upper()
        if guess=="" or len(guess)>1:
            print("Invalid entry. "+"Please enter one and only one letter.")
            continue
        elif guess in guessed_letters:
            print("You already tried that letter.")
            continue
        else:
            return guess

#the meat and potatoes of the code, more or less sets the rules of the game
def play_game():
#ASCII Hangman and attempts code obtained from https://codereview.stackexchange.com/questions/95997/simple-game-of-hangman
    Hangman = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
""")
    print(Hangman[0])
    attempts = len(Hangman) - 1
#puts the word in context of the screen, displaying the amount of blanks to give the user hints as to what to input    
    word=get_word()
    word_length=len(word)
    remaining_letters=word_length
    displayed_word="_"*word_length
#sets the number of guesses and incorrect guesses to 0
    num_wrong=0
    num_guesses=0
    guessed_letters=""
#draws the screen
    draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)
#handles the guesses counter on both ends and the letters you've already used
    while num_wrong < 10 and remaining_letters > 0:
        guess=get_letter(guessed_letters)
        guessed_letters+=guess

        pos=word.find(guess, 0)
        if pos!= -1:
            displayed_word=""
            remaining_letters=word_length
            for char in word:
                if char in guessed_letters:
                    displayed_word+=char
                    remaining_letters -= 1
                else:
                    displayed_word += "_"
        else:
            num_wrong += 1
            attempts -= 1
            print(Hangman[(len(Hangman) - 1) - attempts]) 
          
        num_guesses+=1
        draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)
    print("-"*79)
#prints game over message for win and loss respectively
    if remaining_letters==0:
        print("Congratulations! You got it in", num_guesses, "guesses.")
    else:
        print("Sorry, you lost.")
        print("The word was: ", word)

def main():
#prints the welcome message and handles the user input for wishing to continue or exit
    print("Play the Hangman game! Here you can enter one letter at a time to guess the wordYou may only enter ten incorrect guesses before you lose so good luck!")
#starts the game
    while True:
        play_game()
        print()
        again=input("Do you want to play again (y/n)?: ").lower()
        if again == "y":
            continue
        elif again == "n":
            import winsound
            print("Thank you so much a-for-to playing my game!")
            winsound.PlaySound("Thanks.wav", winsound.SND_FILENAME)
            break
        else:
            print("That is not a valid option, please try again.")

if __name__=="__main__":
    main()
