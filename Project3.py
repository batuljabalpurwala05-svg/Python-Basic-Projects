expenses =[]

def validate_amount():
    while True:
        try:
            amt = float(input("Enter Amount: "))
            if amt > 0:
                return amt
            else:
                print("Amount must be positive!")
        except ValueError:
            print("Invalid amount! Enter a number.")

def add_expense():
    desc = input("Enter description :")
    category = input("Enter category(Food/Travel/Bills/Entertainment/Other) :")
    amount = validate_amount()
    date = int(input("Enter date :"))

    expense = {
        "desc":desc,
        "category":category,
        "amount":amount,
        "date":date
    }
    expenses.append(expense)

    total = 0
    for e in expenses:
        total += e["amount"]

    print("Expense Added! Current Total: Rs.", round(total, 2))

def view_expense():
    if not expenses:
        print("Expense not recorded!")
        return
    print("===== ALL EXPENSES =====")
    for i, e in enumerate(expenses, start=1):
        print(i, ".", e['desc'], "|", e['category'], "| Rs.", round(e['amount'], 2), "|", e['date'])

def category_summary():
    if not expenses:
        print("No expenses recorded!")
        return
    
    summary ={}
    for e in expenses:
        cat =  e["category"]
        summary[cat] = summary.get(cat, 0) + e["amount"]

    print("===== CATEGORY SUMMARY =====")
    for cat, total in summary.items():
        print(cat,": Rs.",total,":.2f")

def get_top_category():
    summary = {}

    for e in expenses:
        summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]

    if not summary:
        return None, 0

    top = max(summary, key=summary.get)
    return top, summary[top]

def budget_report(budget):
    if not expenses:
        print("No expenses recorded!")
        return
    total = sum(e["amount"] for e in expenses)
    remaining = budget - total
    percent = (total / budget) * 100

    print("========= BUDGET REPORT =========")
    print("Total Spent   : Rs.", round(total, 2))
    print("Budget Limit  : Rs.", round(budget, 2))
    print("Remaining     : Rs.", round(remaining, 2))
    print("Used          :", round(percent, 2), "%")

    # Warnings
    if percent>=100:
        print("WARNING: Budget exceeded!")
    elif percent >= 80:
        print("WARNING: You have used 80% of your budget!")
    
    # Top category
    top_cat, amt = get_top_category()
    if top_cat:
        print("Top Category  :", top_cat, "(Rs.", round(amt, 2), ")")

def show_menu():
    print("===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All")
    print("3. Category Summary")
    print("4. Budget Report")
    print("5. Exit")

def main():
    try:
         budget = float(input("Enter Monthly Budget: Rs. "))
    except ValueError:
        print("Invalid budget! Budget limit is 5000")
        budget = 5000.0
    
    while True:
        show_menu()

        try:
            choice = int (input("Enter your choice(1-5) :"))
            if choice == 1:
                add_expense()
            elif choice == 2:
                view_expense()
            elif choice == 3:
                category_summary()
            elif choice == 4:
                budget_report(budget)
            elif choice == 5:
                print("Exiting Program...")
                break
            else:
                print("Invalid choice!")

        except ValueError:
            print("❌ Enter a valid number!")


# Run program
main()
    
