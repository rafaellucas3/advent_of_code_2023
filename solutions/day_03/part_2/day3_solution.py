import os
from math import prod

BASE_DIRECTORY = os.getcwd()
SOLUTION_DIRECTORY = os.path.join(BASE_DIRECTORY, "solutions/day_03/part_1")

class Symbol:
    def __init__(self, symbol, row, index):
        self.symbol = symbol
        self.row = row
        self.index = index
    
    def __repr__(self) -> str:
        return f"Symbol({self.symbol}, {self.row}, {self.index})"
    
    def _get_slice(self, row, start_index, finish_index):
        row_slice = ''
        if start_index > 0 and finish_index < len(row) and row != None:
            row_slice = row[start_index-1:finish_index+1]
        elif start_index == 0 and row != None:
            row_slice = row[start_index:finish_index + 1]
        elif finish_index == len(row) and row != None:
            row_slice = row[start_index - 1:finish_index]
        return row_slice
    

    def _get_numbers_in_a_row(self,row_number, row_data):
        numbers = []
        #keep a copy of the row data for later
        data_str = row_data

        #clear the symbols
        for i, str in enumerate(row_data):
            for char in str:
                if not char.isdigit(): 
                    row_data = row_data.replace(char, ".")
        
        #split the row data into a list of strings
        row_data = row_data.split(".")

        #clear the empty strings
        row_data = [i for i in row_data if i != ""]

        for number in row_data:
            start_index = data_str.find(number)
            numbers.append(Number(int(number), row_number, start_index+1, start_index+len(number)))
            filling = "." * len(number)
            data_str = data_str[:start_index] + filling + data_str[start_index + len(filling):]
        
        return numbers

    #detect numbers around the symbol
    def check_around(self, data):
        previous_numbers = self._get_numbers_in_a_row(self.row - 1, data[self.row - 1]) if self.row > 0 else None
        numbers = self._get_numbers_in_a_row(self.row, data[self.row])
        next_numbers = self._get_numbers_in_a_row(self.row + 1, data[self.row + 1]) if self.row < len(data) - 1 else None

        all_numbers = previous_numbers + numbers + next_numbers

        numbers_around = []

        for number in all_numbers:
            if (number.start_index <= self.index + 1 and number.start_index >= self.index - 1) or (number.finish_index <= self.index + 1 and number.finish_index >= self.index - 1):
                numbers_around.append(number)
        
        if len(numbers_around) > 1:
            return prod([number.value for number in numbers_around])
        
        else:
            return 0

class Number:
    def __init__(self, value, row, start_index, finish_index):
        self.value = value
        self.row = row
        self.start_index = start_index
        self.finish_index = finish_index

    def __repr__(self):
        return f"Number({self.value}, {self.row}, {self.start_index}, {self.finish_index})"
    
if __name__ == "__main__":
        
    with open(f"{SOLUTION_DIRECTORY}/input.txt", "r") as f:	
        data = f.read().splitlines()
    
    symbols = []

    for row_number, row_data in enumerate(data):
        #keep a copy of the row data for later
        data_str = row_data

        #clear the numbers
        for i, str in enumerate(row_data):
            for char in str:
                if char.isdigit(): 
                    row_data = row_data.replace(char, ".")
        
        #split the row data into a list of strings
        row_data = row_data.split(".")

        #clear the empty strings
        row_data = [i for i in row_data if i != ""]

        for symbol in row_data:
            start_index = data_str.index(symbol)
            symbols.append(Symbol(symbol, row_number, start_index+1))

            filling = "."
            data_str = data_str[:start_index] + filling + data_str[start_index + 1:]

    sum = 0
    for symbol in symbols:
        sum += symbol.check_around(data)
    
    print(sum)