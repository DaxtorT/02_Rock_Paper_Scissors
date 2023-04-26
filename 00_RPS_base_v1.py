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

def statement_deco(deco_sides, deco_top_bottom, start_statement, three_line):
    # Sets up decoration for sides of statement and top / bottom
    sides = deco_sides * 3
    single_statement = f"{sides} {start_statement} {sides}"

    top_bottom = deco_top_bottom * len(single_statement)
    big_statement = f"{top_bottom}\n{single_statement}\n{top_bottom}"

    # Outputs either single or triple line statement
    if three_line == 1:
        return single_statement

    elif three_line ==3:
        return big_statement

def instructions():
    intro = statement_deco("*", "-", "How To Play", 1)
    print(intro)
    print("Playing Rock, Paper, Scissors is very simple")
    print("All you have to do is choose an amount of rounds to play, or press enter to play continously")
    print("Then you need to choose either Rock(R), Paper(P), or Scissors(S) to play for each round.")
    print("If you chose 'Continous Mode' you will need to type 'xxx' to stop the rounds and finish the game")
    return ""

# Main Routine goes here
# Constants for program
round_no = 1
rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

yes_no_instructions = "Have you played before? "
yes_no_error = "Please say 'Yes' or 'No'" 
choose_instruction = "What move do you want to make (Rock, Paper, Scissors)? "
choose_error = "Please choose Rock, Paper or Scissors"

# Lists or Dicts of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]
game_summary = []

results_dict = {
('rock', 'paper'): "lost",
('rock', 'scissors'): "won",
('paper', 'rock'): "won",
('paper', 'scissors'): "lost",
('scissors', 'rock'): "lost",
('scissors', 'paper'): "won"}

comparison_dict = {
'r': ('rock'),
'p': ('paper'),
's': ('scissors')}

# Welcome to the game statement
welcome_statement = statement_deco("=", "-", "Welcome to The Rock, Paper, Scissors Game", 3)
print(welcome_statement)
print()

# Ask user if they have played before
played_before = choice_checker(yes_no_instructions, yes_no_error, yes_no_list)

# If 'yes', show instructions
if played_before == "n" or played_before == "no":
    print()
    game_instructions = instructions()
    print(game_instructions)
    print()

else:
    print()

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()
print()

end_game = "no"
while end_game == "no":

    # Rounds Heading
    if rounds == "":
        heading = f"Continous Mode: Round {rounds_played + 1}"
        print_heading = statement_deco("=", "-", heading, 1)
        
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"
        print_heading = statement_deco("-", "-", heading, 1)
        
    print(print_heading)

    # Ask user to choose a move to make (Rock, Paper, Scissors)
    choose = choice_checker(choose_instruction, choose_error, rps_list)
    print()
    
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
        result = ("tie")

    else:
        result = results_dict[(output_word, comp_choice,)]

    # Adding result to list
    game_summary.append(result)

    # Calculates total won, lost and drawn rounds
    if result == "tie":
        result = "It's a Tie"
        rounds_drawn += 1

    elif result == "lost":
        result = ":( You Lose ):"
        rounds_lost += 1

    else:
        result = "! You WIN !"

    # Prints result of the current round
    print(f"Result: {result}")
    print()

# Quick winning rounds calculation
rounds_won = rounds_played - rounds_lost - rounds_drawn

# Calculate all game history
percent_won = rounds_won / rounds_played * 100
percent_lost = rounds_lost / rounds_played * 100
percent_tie = rounds_drawn / rounds_played * 100

# Ask user if the want to see their game history
# If 'yes', show game history
print()
show_history = choice_checker("Do you want to see your game history? ", "Please answer 'Yes' or 'No'", yes_no_list)

if show_history == "yes" or show_history == "y":
    print()
    game_his = statement_deco("*", "-", "Game History", 1)
    print(game_his)
    for game in game_summary:
        print(f"R{round_no}: {game}")
        round_no += 1

    print()
    game_stat = statement_deco("*", "-", "Game Statistics", 1)
    print(game_stat)
    print(f"Win: {rounds_won}, ({percent_won:.0f}%)",
        f"\nLoss: {rounds_lost}, ({percent_lost:.0f}%)",
        f"\nTie: {rounds_drawn}, ({percent_tie:.0f}%)")

else:
    print("No Problem :)")

# Final end game content
print()
end_statement = statement_deco("!", "-", "Thanks for Playing", 3)
print(end_statement)