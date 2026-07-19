import random
import math
number_set = set()
while len(number_set) < 10:
    try:
        num = float(input("Enter number:"))
        number_set.add(num)
    except ValueError:
        print("Please Enter a number")
number_tuple = tuple(number_set)
print("Tuple of number :",number_tuple)
try:
    # Pick 3 random numbers
    random_nums = random.sample(number_tuple, 3)
    print("3 Random Numbers:", random_nums)
    # Square root of sum
    total = sum(number_tuple)

    if total < 0:
        raise ValueError("Sum is negative, cannot take square root.")

    sqrt_value = math.sqrt(total)
    print("Square root of sum:", sqrt_value)

except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("Something went wrong:", e)
