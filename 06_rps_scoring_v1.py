# Rounds won will be calculated (total - draw - lost)
rounds_played = 0
rounds_lost = 0
rounds_draw = 0

# Results for testing purposes
test_results = ["won", "won", "loss", "loss", "tie"]

# Play game
for item in test_results:
    rounds_played += 1

    result = item

    if result == "tie":
        result = "It's a Tie"
        rounds_draw += 1

    elif result == "lost":
        result = "You Lose"
        rounds_lost += 1

# Quick calculations
rounds_won = rounds_played - rounds_lost - rounds_draw

# End of game statements
print()
print(f"Won: {rounds_won}, Drawn: {rounds_draw}, Lost: {rounds_lost}")