import re

def get_max_cubes(cubes):
    max = 0

    for cube in cubes:
        cube = int(cube)
        if cube > max:
            max = cube

    return max


id_pattern = re.compile("Game \d+:")
red_pattern = re.compile("(\d+) red")
blue_pattern = re.compile("(\d+) blue")
green_pattern = re.compile("(\d+) green")

total_power = 0
with open("../input.txt") as file:

    lines = file.readlines()

    for line in lines:

        id_match = id_pattern.findall(line)[0]
        id = int(id_match.lstrip("Game ").rstrip(":"))
        
        game = line[len(id_match):]

        red = red_pattern.findall(game)
        red_max = get_max_cubes(red)

        green = green_pattern.findall(game)
        green_max = get_max_cubes(green)

        blue = blue_pattern.findall(game)
        blue_max = get_max_cubes(blue)

        power = red_max * green_max * blue_max
        total_power += power
        
    print(total_power)