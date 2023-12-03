import os
from math import prod

BASE_DIRECTORY = os.getcwd()
SOLUTION_DIRECTORY = os.path.join(BASE_DIRECTORY, "solutions/day_02/part_1")

#support functions
def process_sets(sets):
    sets = sets.split(", ")
    sets_list = []
    for set in sets:
        set = set.split(" ")
        sets_list.append((set[1], int(set[0])))
    return sets_list

def parse_game(data):
    data = data.split("; ")
    game_dict = {}

    for i, data in enumerate(data):
        if i==0:
            data = data.split(": ")
            game_dict["game_id"] = int(data[0].split(" ")[1])
            game_dict["sets"] = [process_sets(data[1])]
        else:
            game_dict["sets"].append(process_sets(data))
    return(game_dict)

class Game:
    def __init__(self, game_id, sets, limit_dict):
        self.id = game_id
        self.sets = sets
        self.limit_dict = limit_dict

    def __repr__(self):
        return f"Game {self.game_id} with {len(self.sets)} sets"
    
    @property
    def is_valid(self):
        for set in self.sets:
            for color, value in set:
                if value > self.limit_dict[color]:
                    return False
        return True
    
    @property
    def minimum_cube_colors(self):
        colors = {}
        for set in self.sets:
            for color, value in set:
                if color not in colors:
                    colors[color] = value
                else:
                    colors[color] = max(colors[color], value)
        return colors
    
    @property
    def power(self):
        return prod([x for x in self.minimum_cube_colors.values()])

if __name__ == "__main__":
    with open(f"{SOLUTION_DIRECTORY}/input.txt") as f:
        data = f.read().splitlines()
    
    data_parsed = [parse_game(game) for game in data]

    limits = {'red': 12, 'green': 13, 'blue': 14}

    games = [Game(game["game_id"], game["sets"], limits) for game in data_parsed]

    sum_valid_game_ids = 0
    for game in games:
        if game.is_valid:
            sum_valid_game_ids += game.id

    print(f"Sum of valid game ids: {sum_valid_game_ids}")

    # Part 2
    minimum_cube_colors = [game.minimum_cube_colors for game in games]
    print(f"Minimum cube colors: {minimum_cube_colors}")

    powers = [game.power for game in games]    
    print(f"Powers: {powers}")
    
    sum_of_powers = sum(powers)
    print(f"Sum of powers: {sum_of_powers}")