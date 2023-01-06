import random

def decision_maker():
    chance = random.randrange(1, 10+1)
    guess = float(input("Pick a number, either 1 or 2: "))
    if chance == guess:
        print("Heads!")
    else:
        print("Tails!")

def main():
    decision_maker()
main()
