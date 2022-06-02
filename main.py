import random

print("*** Rock-Paper-Scissors Game ***")
game_choices = ["R", "P", "S"]
game_words = { "R": "Rock", "P": "Paper", "S": "Scissors" }

print("""Choose your move (R, P, S)
    Note
            R means Rock
            P means Paper
            S means Scissors           
""")

user_choice = str(input("What's your choice? "))
user_choice = user_choice.upper()

while user_choice not in game_choices:
    print("Error, your choice is not valid")
    print("""Choose your move (R, P, S)
    Note
            R means Rock
            P means Paper
            S means Scissors           
""")
    user_choice = str(input("What's your choice? "))
    user_choice = user_choice.upper()

computer_choice = random.choice(game_choices)


while user_choice == computer_choice:
    print(f"Player ({game_words[user_choice]}) : CPU ({game_words[computer_choice]})")
    print("Tie, choose again")
    print("""Choose your move (R, P, S)
    Note
            R means Rock
            P means Paper
            S means Scissors           
""")

    user_choice = str(input("What's your choice? "))
    computer_choice = random.choice(game_choices)
    user_choice = user_choice.upper()
    while user_choice not in game_choices:
        print("Error, your choice is not valid")
        print("""Choose your move (R, P, S)
        Note
                R means Rock
                P means Paper
                S means Scissors           
    """)
        user_choice = str(input("What's your choice? "))
        user_choice = user_choice.upper()
        computer_choice = random.choice(game_choices)
print(f"Player ({game_words[user_choice]}) : CPU ({game_words[computer_choice]})")


if user_choice == "R" and computer_choice == "S":
    print("Player wins")
if user_choice == "P" and computer_choice == "R":
    print("Player wins")
elif user_choice == "S" and computer_choice == "P":
    print("Player wins")
else:
    print("CPU wins")

