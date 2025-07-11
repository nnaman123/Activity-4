#calculate the square root of a number
import math
def calculate_square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(number)
#ask the user for a number
number = float(input("Enter a number to calculate its square root: "))
try:
    result = calculate_square_root(number)
    print(f"The square root of {number} is {result}")
except ValueError as e:
    print(e)
