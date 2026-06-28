square = lambda x: x*x
try:
    numbers = list(range(1, 21))
    # Store squares using lambda
    squares_list = list(map(square, numbers))
    print("All squares:", squares_list)
    # Filter only even squares
    for num in squares_list:
        if num % 2 == 0:
            print("Even numbers :",num)
except Exception as e:
    print("An error occurred:", e)