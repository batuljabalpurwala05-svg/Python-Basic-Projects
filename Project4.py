import random

# -------- LOAD QUESTIONS --------
def load_questions():
    return [
        ("Which data type is immutable?", "List", "Dictionary", "Tuple", "Set", "C"),
        ("Which keyword is used for function?", "def", "func", "function", "define", "A"),
        ("Which symbol is used for comments?", "#", "//", "/* */", "--", "A"),
        ("Which data type stores key-value pairs?", "List", "Tuple", "Dictionary", "Set", "C"),
        ("Which loop is used when condition is true?", "for", "while", "loop", "repeat", "B"),
        ("Which operator is for equality?", "=", "==", "!=", "<>", "B"),
        ("Which function gives length?", "size()", "count()", "len()", "length()", "C"),
        ("Which module is used for random?", "math", "random", "os", "sys", "B"),
        ("Which keyword is for condition?", "if", "for", "while", "loop", "A"),
        ("Which collection is unordered?", "List", "Tuple", "Set", "String", "C")
    ]

# -------- DISPLAY QUESTION --------
def display_question(q, index):
    print("Q",index,":",q[0])
    print("A.",q[1])
    print("B.",q[2])
    print("C.",q[3])
    print("D.",q[4])

# -------- GET ANSWER --------
def get_answer():
    while True:
        try:
            ans = input("Your Answer (A/B/C/D): ").strip().upper()
            if ans in ["A", "B", "C", "D"]:
                return ans
            else:
                print("Enter only A, B, C, or D!")
        except:
            print("Invalid input!")

# -------- CALCULATE GRADE --------
def calculate_grade(percent):
    if percent >= 90:
        return "A+"
    elif percent >= 80:
        return "B+"
    elif percent >= 70:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 50:
        return "D"
    else:
        return "F"
    
def evaluate_quiz(questions):
    score = 0
    wrong_answers = []

    for i, q in enumerate(questions, start=1):
        display_question(q, i)
        user_ans = get_answer()

        if user_ans == q[5]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect! Correct answer:",q[5])
            wrong_answers.append((q[0], user_ans, q[5]))

    return score, wrong_answers

# -------- SHOW WRONG ANSWERS --------
def show_wrong_answers(wrong_answers):
    if not wrong_answers:
        return

    print("===== WRONG ANSWERS =====")
    for q, user, correct in wrong_answers:
        print("Q:",q)
        print("Your Answer:", user,"| Correct:",correct)

def show_report(name, roll, score, total, wrong_answers):
    percent = (score / total) * 100
    grade = calculate_grade(percent)

    print("====== RESULT REPORT ======")
    print("Name    :",name)
    print("Roll No :",roll)
    print("Score   :",score/total)
    print("Percent :",percent,"%")
    print("Grade   :",grade)
    print("Result  :", "PASS" if percent >= 50 else "FAIL")

    show_wrong_answers(wrong_answers)

# -------- MAIN --------
def main():
    print("===== PYTHON QUIZ SYSTEM =====")
    name = input("Enter Name: ")
    try:
        roll = int(input("Enter Roll No: "))
    except ValueError:
        print("Invalid roll number! Setting default = 0")
        roll = 0

    questions = load_questions()
    # Shuffle questions
    random.shuffle(questions)

    score, wrong_answers = evaluate_quiz(questions)
    show_report(name, roll, score, len(questions), wrong_answers)

# Run program
main()
