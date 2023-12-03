import os

BASE_DIRECTORY = os.getcwd()
SOLUTION_DIRECTORY = os.path.join(BASE_DIRECTORY, "solutions/day_01/part_2")

def parse_string(search_result):
    """Parse a string and return the parsed string."""
    result = ""
    for key, value in search_result:
        result += value
    return result
        
def search(string, search_dict):
    """Search a string for a key in a dictionary recursevelly and return the index of the key and the value."""    
    search_result = []
    for key, value in search_dict.items():
        string_copy = string
        cut_char = 0
        index = string_copy.find(key)
        while index != -1:
            search_result.append((cut_char + index, value))
            cut_char += len(string_copy[0:index+len(key)])
            string_copy = string_copy[index+len(key):len(string_copy)]
            index = string_copy.find(key)
    
    search_result.sort(key=lambda x: x[0])

    return parse_string(search_result)

def main():
    search_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9"
    }

    with open(f"{SOLUTION_DIRECTORY}/input.txt") as f:
        data = f.read().splitlines()

    searched_data = list(map(lambda x: search(x, search_dict), data))
    print(searched_data)

    secret = []
    for cal_value in searched_data:
        if len(cal_value) == 1:
            secret.append(int(f"{cal_value}{cal_value}"))
        else:
            secret.append(int(f"{cal_value[0]}{cal_value[-1]}"))
    
    print(secret)
    print(sum(secret))

if __name__ == "__main__":
    main()