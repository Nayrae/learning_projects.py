import random 


def game(user_score, enemy_score):
    weapons = ["Rock", "Paper", "Scissors"]
    while True:
        print("Your actual score is ", user_score, " while your enemy score is ", enemy_score)
        
        enemy = random.choice(weapons)

        while True:
            choice = input("Choose your weapon: 'Rock', 'Paper', 'Scissors'(or press enter to quit): ")
            if choice == "":
                break
            if choice not in weapons:
                print("Please, type the right weapon!")
                continue
            else:
                break
            

        if choice == "Rock" and enemy == "Scissors":
            print("You WON!")
            user_score += 1

        elif choice == "Paper" and enemy == "Rock":
            print("You WON!")
            user_score += 1

        elif choice == "Scissors" and enemy == "Paper":
            print("You WON!")
            user_score += 1        

        elif choice == enemy:
            print("It's a DRAW!")

        elif choice == "":
            break

        else:
            print("You LOST!")
            enemy_score += 1

        print("Press enter to quit, or choose your weapon to keep going!")
        


game(0, 0)