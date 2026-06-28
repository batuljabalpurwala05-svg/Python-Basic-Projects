import math

try:
    # Take sentence input
    sentence = input("Enter a sentence: ")
    # Extract words and store unique ones using set
    words = sentence.split()
    unique_words = set(words)
    # Sort unique words
    sorted_words = sorted(unique_words)
    print("Unique words in sorted order:", sorted_words)
    # Count of unique words
    count = len(unique_words)
    # Square using math module
    result = math.pow(count, 2)
    print("Square of total unique words:", result)

except Exception as e:
    print("An error occurred:", e)
