import random # Importing the random module

def rand_num(): 
    return random.randint(1, 100) # Returns a random number between 1 and 100

def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    num = rand_num() # Assigns a random number to the variable num
    guess = int(input("I think the number is: "))
    counter = 0
    while guess != num:
        if num - guess >= 0:
            print("Too bad, try again.", "\nThe number should be higher" )
        else:
            print("Too bad, try again.", "\nThe number should be lower" )
        guess = int(input("I think the number is: "))
        counter +=1
    if num == guess:
        print("Congrats, it only took you ", counter, "tries!")


rand_num()
main()