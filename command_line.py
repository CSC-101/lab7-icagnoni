import sys
from convert import str_to_float

def command_line_arguments() -> float:
    numbers = []
    for arg in sys.argv[1:]:
        number = str_to_float(arg)
        if number is not None:
            numbers.append(number)
    return sum(numbers)

if __name__ == '__main__':
    print(sys.argv)