def analyze_string(s):
    print("Length of the string :",len(s))
    print("reverse of the string :",s[::-1])
    count = 0
    for ch in s.lower():
        if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
            count += 1
    print("Number of vowels:", count)

    print("Character index:")
    for i in range(len(s)):
        print("Character:",s[i],"|Positive Index:",i,"Negative Index:",i - len(s))

string = input("Enter a string :")
analyze_string(string)