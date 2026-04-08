balance = 10000
withdraw = int(input("How much money would you like to withdraw?"))
if withdraw <= balance:
    print("withdrawal complete!, balance is now:", balance - withdraw)
elif withdraw > balance:
    print("Insufficient funds")

temp = int(input("What is the current temperature outside?"))
is_raining = input("Is it raining?")

if temp < 20 and is_raining == "yes":
    print("Wear a warm jacket and bring an umbrella")
elif temp < 20 and is_raining == "no":
    print("Just bring a warm jacket")
elif temp > 20 and is_raining == "yes":
    print("Use a T-shirt and bring an umbrella")
elif temp >= 20:
    print("A T-shirt is fine")
