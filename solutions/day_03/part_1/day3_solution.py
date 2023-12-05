import os

BASE_DIRECTORY = os.getcwd()
SOLUTION_DIRECTORY = os.path.join(BASE_DIRECTORY, "solutions/day_03/part_1")

class Number:
    def __init__(self, value, row, start_index, finish_index):
        self.value = value
        self.row = row
        self.start_index = start_index
        self.finish_index = finish_index
    
    def __repr__(self):
        return f"Number({self.value}, {self.row}, {self.start_index}, {self.finish_index})"
    
    def _get_symbols_mask(self, row:str):
        for char in row:
            if char.isdigit():
                row = row.replace(char, ".")
        return row
    
    def _get_slice(self, row, start_index, finish_index):
        row_slice = ''
        if start_index > 0 and finish_index < len(row) and row != None:
            row_slice = row[start_index-1:finish_index+1]
        elif start_index == 0 and row != None:
            row_slice = row[start_index:finish_index + 1]
        elif finish_index == len(row) and row != None:
            row_slice = row[start_index - 1:finish_index]
        return row_slice
    
    def is_part_number(self, data):        
        previous_row = data[self.row - 1] if self.row > 0 else None
        data_row = data[self.row]
        next_row = data[self.row + 1] if self.row < len(data) - 1 else None

        previous_row_symbols = self._get_symbols_mask(previous_row) if previous_row != None else None
        data_row_symbols = self._get_symbols_mask(data_row)
        next_row_symbols = self._get_symbols_mask(next_row) if next_row != None else None 

        previous_row_slice = self._get_slice(previous_row_symbols, self.start_index, self.finish_index) if previous_row != None else None
        data_row_slice = self._get_slice(data_row_symbols, self.start_index, self.finish_index)
        next_row_slice = self._get_slice(next_row_symbols, self.start_index, self.finish_index) if next_row != None else None

        previous_row_symbols_sanitized = previous_row_slice.replace(".", "") if previous_row != None else None
        data_row_symbols_sanitized = data_row_slice.replace(".", "")
        next_row_symbols_sanitized = next_row_slice.replace(".", "") if next_row != None else None  

        if previous_row_symbols_sanitized != None:
            if len(previous_row_symbols_sanitized) > 0:
                return True
        
        if next_row_symbols_sanitized != None:
            if len(next_row_symbols_sanitized) > 0:
                return True
        
        if data_row_symbols_sanitized != None:
            if len(data_row_symbols_sanitized) > 0:
                return True

        return False

if __name__ == "__main__":
        
    with open(f"{SOLUTION_DIRECTORY}/input.txt") as f:
        data = f.read().splitlines()
    
    numbers = []

    for row_number, row_data in enumerate(data):
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
            numbers.append(Number(int(number), row_number, start_index, start_index+len(number)))

            filling = "." * len(number)
            data_str = data_str[:start_index] + filling + data_str[start_index + len(filling):]

    part_numbers = [number.value for number in numbers if number.is_part_number(data)]
    print(sum(part_numbers))