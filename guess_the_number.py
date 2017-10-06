# Created by: Julie Nguyen
# Created on: Oct 2017
# Created for: ICS3U
# This program is a guessing game where the user must input the number 5 (the correct number) in order to 
# win
# Modified on: Oct 2017
# added an if statement, removed constant of 5 and replaced it with random integer code

import ui
from numpy import random

# random number to guess
guessed_number = random.randint(1, 10)

def check_answer_button_touch_up_inside(sender):
    # checks if the user's guess was right or wrong
    
    # input
    number_entered = int(view['enter_guess_textfield'].text)
    
    # process
    global guessed_number
    if number_entered == guessed_number:
        #output
        view['answer_label'].text = "Bingo! You are correct!"
    else:
        view['answer_label'].text = "Sorry, the number is " + str(guessed_number) + "!"

view = ui.load_view()
view.present('full_screen')
