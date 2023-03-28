rps_list = ["rock", "paper", "scissors"]
comp_index = 0
# Generate all possible options
for item in rps_list:
    users_index = 0
    for item in rps_list:
        user_choice = rps_list[users_index]
        comp_choice = rps_list[comp_index]
        users_index += 1

        # Compare user and computer choices
        # Dictionary of possible results
        results_dict = {
        ('rock', 'paper'): "You Lose",
        ('rock', 'scissors'): "You WIN",
        ('paper', 'rock'): "You WIN",
        ('paper', 'scissors'): "You Lose",
        ('scissors', 'rock'): "You Lose",
        ('scissors', 'paper'): "You WIN",
        }

        # Get the result from the dictionary based on the user and computer choices
        if user_choice == comp_choice:
            result = ("It's a Tie")

        else:
            result = results_dict[(user_choice, comp_choice)]

        print(f"You chose {user_choice}, the computer chose {comp_choice}. \nResult: {result} ")

    comp_index += 1
    print()