
# Main Routine goes here
# Set-Up or Constants go here
rounds_played = 0

choose_instruction = "Please choose rock (r), paper (p) or scissors (s)"

# Ask number or infinite
num_inf = input("Do you want to play a 'Number' or rounds or 'Infinte'? ").lower()
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
