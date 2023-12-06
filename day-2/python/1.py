import re

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

id_pattern = re.compile("Game \d+:")
red_pattern = re.compile("(\d+) red")
blue_pattern = re.compile("(\d+) blue")
green_pattern = re.compile("(\d+) green")

total_of_possible_games = 0

with open("../input.txt") as file:

    lines = file.readlines()

    for line in lines:

        id_match = id_pattern.findall(line)[0]
        id = int(id_match.lstrip("Game ").rstrip(":"))

        game = game = line[len(id_match):]
        
        red = red_pattern.findall(game)
        red_game = not any(int(count) > RED_MAX for count in red)

        green = green_pattern.findall(game)
        green_game =  not any(int(count) > GREEN_MAX for count in green)

        blue = blue_pattern.findall(game)
        blue_game =  not any(int(count) > BLUE_MAX for count in blue)


        if False in (red_game, green_game, blue_game):
            continue

        total_of_possible_games += id

    print(total_of_possible_games)
            



            


 



        
    
     