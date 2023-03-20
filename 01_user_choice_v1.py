# Functions go here
def choice_checker():
    valid = False
    while not valid:
        response = input("What move do you want to play? ").lower()

        if response == "r" or response == "rock":
            return "Rock"
        
        elif response == "p" or response == "paper":
            return "Paper"
                
        elif response == "s" or response == "scissors":
            return "Scissors"
        
        else:
            print("Please enter either Rock, Paper or Scissors")
            print()

# Main Routine goes here
# Ask user for choice and check it's valid
print()
user_choice = choice_checker()

# Print out choice for comparison purposes
print(f"You chose {user_choice}")
print()