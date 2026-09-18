# get valid input
from math import inf

def get_valid_input(min: int, max: int):
    '''Repeatedly requires a value input until it is within bounds.'''
    while True:
        value = int(input())
        if min <= value and value <= max:
            return value
        else:
            print(f"Must between {min} and {max}. Try again: ", end='')

print("Insert your age: ", end='')
# age = get_valid_input(0, inf)
age = get_valid_input(0, 130)
print(f"Your age is {age}!")
