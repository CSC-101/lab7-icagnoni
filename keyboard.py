from typing import List
from convert import str_to_float

def gather_numbers() -> List[float]:
    numbers = []
    while True:
        user_input = input("Enter a number: ")
        if user_input.lower() == "done":
            break
        number = str_to_float(user_input)
        if number is not None:
            numbers.append(number)
        else:
            print("Invalid. Enter a valid number.")
    return numbers