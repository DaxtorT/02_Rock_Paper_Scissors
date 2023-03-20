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

# Main Routine goes here
# List for choice
user_list = ["rock", "paper", "scissors", "xxx"]

# Loop for testing
user_choice = ""
while user_choice != "xxx":

    # Ask user for choice and check its valid
    user_choice = choice_checker("What move do you want to play? ", "Please enter either Rock, Paper or Scissors", user_list)

    # Print out choice for comparison purposes
    print(f"You chose {user_choice}")
    print()