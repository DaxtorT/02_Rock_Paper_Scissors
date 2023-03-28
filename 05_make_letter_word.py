# Main Routine goes here
# Dicts of valid responses
comparison_dict = {
    'r': ['rock'],
    'p': ['paper'],
    's': ['scissors']
}

choose = input("Please enter move? ")

# Converts single letter response into word for comparison(if required)
if len(choose) == 1:
    input_letter = choose
    if input_letter in comparison_dict:
        output_word = comparison_dict[input_letter]

elif len(choose) > 1:
    output_word = choose

print(output_word)