"""
    KenzLedger
"""

# Global variables
transactions = []
running = True

# Functions
def add_transaction(transactions):
    transaction = {}
    
    while True:
        amount = input("\nAmount (or \"q\" to cancel): ")
        if amount == "q":
            return
        else:
            try:
                amount = int(amount)
                transaction["amount"] = amount
                break
            except ValueError:
                print("Invalid input.\nPlease enter an amount.")
                continue
                
    while True:
        category = input("Category (or \"q\" to cancel): ")
        if category == "q":
            return
        elif category == "":
            print("Category cannot be empty.")
            continue
        else:
            transaction["category"] = category
            break

    description = input("Add description (or \"q\" to cancel): ")
    if description == "q":
        return
    elif description == "":
        transaction["description"] = "No description"
    else:
        transaction["description"] = description
            
    transactions.append(transaction)
    print(transactions)
    print("\nTransaction added!")

def view_balance():
    print("\nView Balance selected...")

def view_reports():
    print("\nView Reports selected...")

# Loop to keep app running
while running:
    print("""\n=== KenzLedger ===
1. Add Transaction
2. View Balance
3. View Reports
4. Exit\n""")
    
    try:
        user_input = int(input("Choose an option (1-4): "))
    except ValueError:
        print("\nInvalid input.\nPlease enter a number (1-4).")
        continue

    if user_input == 1:
        add_transaction(transactions)
    elif user_input == 2:
        view_balance()
    elif user_input == 3:
        view_reports()
    elif user_input == 4:
        print("\n=== App closed ===")
        running = False
    else:
        print("\nInvalid option.\n")
