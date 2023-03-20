# Functions go here
def choice_checker(question, error):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "r" or response == "rock":
            return "Rock"
        
        elif response == "p" or response == "paper":
            return "Paper"
                
        elif response == "s" or response == "scissors":
            return "Scissors"
        
        else:
            print(error)
            print()

# Main Routine goes here
# Ask user for choice and check it's valid
print()
user_choice = choice_checker("What move do you want to play? ", "Please enter either Rock, Paper or Scissors")

# Print out choice for comparison purposes
print(f"You chose {user_choice}")
print()