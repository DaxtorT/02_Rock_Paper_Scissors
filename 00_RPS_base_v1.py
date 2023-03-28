import random

# Functions go here
def choice_checker(question, error, valid_list):
    while True:
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
choose_error = "Please choose Rock, Paper or Scissors"
instructions = "These will be instructions"

# Lists or Dicts of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

results_dict = {
('rock', 'paper'): "You Lose",
('rock', 'scissors'): "You WIN",
('paper', 'rock'): "You WIN",
('paper', 'scissors'): "You Lose",
('scissors', 'rock'): "You Lose",
('scissors', 'paper'): "You WIN",}

comparison_dict = {
    'r': ('rock'),
    'p': ('paper'),
    's': ('scissors')
}

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

    # Ask user to choose a move to make (Rock, Paper, Scissors)
    choose = choice_checker(choose_instruction, choose_error, rps_list)

    # End game if exit code is typed
    if choose == "xxx":
        break

    elif choose == "":
        choose = "Nothing"

    # Converts single letter response into word for comparison(if required)
    if len(choose) == 1:
        input_letter = choose
        if input_letter in comparison_dict:
            output_word = comparison_dict[input_letter]

    elif len(choose) > 1:
        output_word = choose

    # Rest of loop / game
    print(f"Your Choice: {output_word}")

    rounds_played += 1
    
    # End game if # of rounds has been played
    if rounds_played == rounds:
            end_game = "yes"

    # Generate random move for computer
    comp_choice = random.choice(rps_list [:-1])
    print(f"Computer Choice: {comp_choice}")

    # Compare user's move with computer's move
    # Get the result from the dictionary based on the user and computer choices
    if output_word == comp_choice:
        result = ("It's a Tie")

    else:
        result = results_dict[(output_word, comp_choice)]

    # Prints result of the current round
    print(f"Result: {result}")

# Ask user if the want to see their game history
# If 'yes', show game history


# Final end game content
print()
print("Thanks for Playing")