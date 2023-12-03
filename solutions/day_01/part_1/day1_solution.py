import os

BASE_DIRECTORY = os.getcwd()
SOLUTION_DIRECTORY = os.path.join(BASE_DIRECTORY, "solutions/day_01/part_1")

def filter_string(string:str) -> str:
    '''Return only the digits from a string.'''
    return "".join([char for char in string if char.isdigit()])

if __name__ == "__main__":

    with open(f"{SOLUTION_DIRECTORY}/input.txt") as f:
        data = f.read().splitlines()

    filtered_data = list(map(filter_string, data))

    secret = 0

    for cal_value in filtered_data:
        if len(cal_value) == 1:
            secret += int(f"{cal_value}{cal_value}")
        else:
            secret += int(f"{cal_value[0]}{cal_value[-1]}")
    
    print(secret)