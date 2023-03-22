import random

# Functions go here
def choice_checker(question, error, valid_list):
    valid = False
    while not valid:
        # Ask user for choice (and force lowercase)
        response = input(question).lower()

        # Runs through list and if response is an item in list (or first letter), the full name is returned
        for item in valid_list:
            if response == item[0] or response == item:
                return response

        # Output error if response not in list        
        print(error)
        print()

def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an integer that is more than 0"

        # If infinite mode not chosen, check response is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to start of loop
                if response < 1:
                    print(round_error)
                    continue

            # If response is not an integer go back to start of loop
            except ValueError:
                print(round_error)
                continue

        return response



# Main Routine goes here
# Constants for program
rounds_played = 0
yes_no_instructions = "Have you played before? "
yes_no_error = "Please say 'Yes' or 'No'" 
choose_instruction = "What move do you want to make (Rock, Paper, Scissors)? "
choose_error = "Please choose Rock (R), Paper (P) or Scissors (S)"
instructions = "These will be instructions"

# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before
# If 'yes', show instructions
played_before = choice_checker(yes_no_instructions, yes_no_error, yes_no_list)

if played_before == "n":
    print(instructions)
    print()

else:
    print()

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if rounds == "":
        heading = f"Continous Mode: Round {rounds_played + 1}"
        
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"
        
    print(heading)
    choose = choice_checker(choose_instruction, choose_error, rps_list)

    # End game if exit code is typed
    if choose == "xxx":
        break

    if choose == "":
        choose = "nothing"

    # Rest of loop / game
    print(f"You chose {choose}")

    rounds_played += 1
    
    # End game if # of rounds has been played
    if rounds_played == rounds:
            end_game = "yes"


# Generate random move for computer


# Compare user's move with computer's move


# Ask user if the want to see their game history
# If 'yes', show game history


# Final end game content
print()
print("Thanks for Playing")