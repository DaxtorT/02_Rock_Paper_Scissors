def choice_checker(question, error, valid_list):
    valid = False
    while not valid:
        # Ask user for choice (and force lowercase)
        response = input(question).lower()

        # Runs through list and if response is an item in list (or first letter), the full name is returned
        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # Output error if response not in list        
        print(error)
        print()

def num_checker(question, min_value, max_value):
    keep_going = ""
    while keep_going == "":
        try:
            # Ask the question
            response = int(input(question))

            # If the amount is too low / too high give
            if  min_value < response <= max_value:
                return response

            # Output error
            elif response < min_value + 1:
                print("error_1")

            elif response > max_value:
                print("error_2")
        
        except ValueError:
            print("error_3")

# Main Routine goes here
# Set-Up or Constants go here
rounds_played = 0

mode_choice_list = ["infinite", "number"]

choose_instruction = "Please choose rock (r), paper (p) or scissors (s)"

# Ask number or infinite
num_inf = choice_checker("Do you want to play a 'Number' or rounds or 'Infinte'? ", 
                         "Please choose infinite / number",mode_choice_list)
print(f'you chose {num_inf}')

if num_inf == "number":
    # Ask how many rounds
    response = int(input("How many rounds do you want to play? "))

    # Check rounds valid
    if 1 < response < 100:
        num_rounds = response

    # Outputs error if needed
    else:
        print("Please choose a number of rounds to play, between 1 and 100")

elif num_inf == "infinite":
    # Sets rounds infinite
    num_rounds = "Continous"

else:
    # Outputs error if needed
    print("Please choose either 'Number' or 'Infinite'")

# Output # rounds to play
print(f"You have asked to play {num_rounds} rounds")

# Loop # of rounds



# Error when running program
# Do i need to set a varible to something before using it, like above
