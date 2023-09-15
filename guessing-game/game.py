"""A number-guessing game."""
import random
import time
# Put your code here
# greet and ask for name


def greeting_ask_name():
    
    player_name = get_input("Hello! What is your name? ")    

    return player_name


# ask for the low and high for the game range     

def get_range():
    
    low_range = get_int_input("Please select a low number: ")
    low_range = int(low_range)

    high_range = get_int_input("Please select a high number: ")
    high_range = int(high_range)

    winning_number = random.randint(low_range, high_range)

    return low_range, high_range, winning_number


# player's guess lol just shut it down ill start it back up

def get_guess():
    
    while True:
        
        player_guess = get_int_input("Enter your guess here: ")
             
        if player_guess not in range(low_range, high_range+1):
            print("This number is not in range, please provide an answer between", low_range, "and", high_range, "to continue.")
            continue

        return player_guess


# written with Ray's help
def get_input(prompt):
    result = input(prompt)
    if result == "exit":
        print("Thank you for playing")
        exit()
    
    return result


#  written with Ray's help
def get_int_input(prompt):
    
    while True:
        result = get_input(prompt)
        try:
            result = int(result)
        except:
            print("use an integer ")
            continue
            
        return result


# guess a number, if correct - end the game and congratulate the player, if wrong provide a hint if it is too low or too high



player_name = greeting_ask_name()
low_range, high_range, winning_number = get_range()
found_correct_answer = False
guess_count = 0

while found_correct_answer is False:
    player_guess = get_guess()
    guess_count += 1 



    if player_guess == winning_number:
        
        print("Congratulations! You picked the right number in", guess_count, "guesses!")
        found_correct_answer = True
    
    elif player_guess < winning_number:
        print("Your guess is too low.")
    
    elif player_guess > winning_number:
        print("Your guess is too high.")
           

      




#Collection of my less than ideal variables


# player_name = greeting_ask_name()
# low_range, high_range = get_range()
# winning_number = random.randint(low_range,high_range)
# result = game_processing()
# player_guess = get_guess()
# guess_count = 1

