import random 



def roll():
    min_roll = 1
    max_roll = 6
    roll = random.randint(min_roll, max_roll)
    return roll
        

while True:
        players = input("Please, insert a number of players (2-4): ")
        if players.isdigit():
              players = int(players)
              if 2 <= players <= 4:
                    break
              else:
                    print("Whoa, i think you're wrong buddy, check again!")
              
max_score = 50
player_scores = [0 for player_index in range(players)]

while max(player_scores) <= max_score:
      for player_index in range(players):
        print("\nPlayer ", player_index+1, " turn.\n")
        current_score = 0
        while True:
            value = roll()
            keep_roll = input("Would you like to roll?(y): ")
            if keep_roll.lower() != "y":
                    break
            else:
                if value == 1:
                        print("You rolled 1, turn ended")
                        current_score = 0
                        break
                else:
                    print("Player number ", player_index+1, " just rolled: ", value)
                    current_score += value
                    
        
        player_scores[player_index] += current_score
        print("Your current score is: ", player_scores[player_index])
        if player_scores[player_index] >= 50: 
              print("Diocan, hai vinto vecchio!")
              break
