import random

print("-----THE ANIMALS-----")
animals = ["Lion", "Tiger", "Elephant", "Monkey", "Panda"]

for a in animals:
    print("-", a)
    
print()

name = input("What is your name? ")
user_guess = input("Guess a random animal from the list: ").strip().title()
cpu_choice = random.choice(animals)

if user_guess == cpu_choice:
    print(f"You matched correctly {name}! You made a new friend: Mr. {cpu_choice}!")
else:
    print(f"Sorry {name}, you were wrong. The computer picked {cpu_choice}.")
