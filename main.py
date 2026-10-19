"""
    KenzLedger
"""

# Imports
import json
import kenz_ui as ui

# App Header
ui.big_title("KenzLedger")

# Variables
running = True

# Functions
def load_transactions(filename):
    try:
        with open(filename, "r") as file:
            transactions = json.load(file)
        return transactions
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_transactions(transactions, filename):
    with open(filename, "w") as file:
        json.dump(transactions, file, indent=4)

def add_transaction(transactions):
    ui.header("=== Add Transaction ===")
    transaction = {}

    while True:
        type_of_transaction = input("\nType (i/e for income/expense, or \"q\" to cancel): ")
        if type_of_transaction == "q":
            ui.cutter()
            return
        elif type_of_transaction.lower() == "income" or type_of_transaction.lower() == "i":
            transaction["type"] = "income"
            break
        elif type_of_transaction.lower() == "expense" or type_of_transaction.lower() == "e":
            transaction["type"] = "expense"
            break
        else:
            print("Invalid option.")
            continue
            
    while True:
        amount = input("Amount (or \"q\" to cancel): ")
        if amount == "q":
            ui.cutter()
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
            ui.cutter()
            return
        elif category == "":
            print("Category cannot be empty.")
            continue
        else:
            transaction["category"] = category
            break

    description = input("Add description (or \"q\" to cancel): ")
    if description == "q":
        ui.cutter()
        return
    elif description == "":
        transaction["description"] = "No description"
    else:
        transaction["description"] = description
            
    transactions.append(transaction)
    save_transactions(transactions, "transactions.json")
    print("\nTransaction added! ✔️")
    ui.cutter()

def view_balance(transactions):
    ui.header("=== View Balance ===")
    if not transactions:
        print("\nNo transactions yet.")
        ui.cutter()
        return

    total_expense = 0
    total_income = 0
    no_of_transactions = len(transactions)
    
    for transaction in transactions:
        tx_type = transaction.get("type", "expense")
        
        if tx_type == "expense":
            total_expense += transaction["amount"]
        elif tx_type == "income":
            total_income += transaction["amount"]

    balance = total_income - total_expense
    balance_str = f"-₦{abs(balance):,}" if balance < 0 else f"₦{balance:,}"
    
    print(f"\nTotal income: ₦{total_income:,}\nTotal expenses: ₦{total_expense:,}\n\nNet balance: {balance_str}\nNumber of transactions: {no_of_transactions}")
    ui.cutter()
    
def view_reports(transactions):
    ui.header("=== View Reports ===")
    if not transactions:
        print("\nNo transactions yet.")
        ui.cutter()
        return

    income_report = {}
    expense_report = {}
    income_count = 0
    expense_count = 0
    total_income = 0
    total_expense = 0
    

    for transaction in transactions:
        tx_type = transaction.get("type", "expense")
        cat = transaction["category"]
        amt = transaction["amount"]

        if tx_type == "income":
            income_count += 1
            if cat not in income_report:
                income_report[cat] = 0
            income_report[cat] += amt
            total_income += amt
            
        elif tx_type == "expense":
            expense_count += 1
            if cat not in expense_report:
                expense_report[cat] = 0
            expense_report[cat] += amt
            total_expense += amt

    if not income_report:
        print("\n===» Income: No income transaction.")
    else:
        print(f"\n===» Income: {income_count} transactions")
        for cat, total in income_report.items():
            print(f" {cat:<12} ₦{total:,}")
        print(f"\nTotal income is ₦{total_income:,}")

    if not expense_report:
        print("\n===» Expense: No expense transaction.")
    else:
        print(f"\n===» Expense: {expense_count} transactions")
        for cat, total in expense_report.items():
            print(f" {cat:<12} ₦{total:,}")
        print(f"\nTotal expense is ₦{total_expense:,}")
            
    ui.cutter()
    balance_num = total_income - total_expense
    balance_str = f"-₦{abs(balance_num):,}" if balance_num < 0 else f"₦{balance_num:,}"
    print(f"Total Income: ₦{total_income:,}\nTotal Expense: ₦{total_expense:,}\nBalance: {balance_str}")
    ui.cutter()

# Load transactions.json file
transactions = load_transactions("transactions.json")

# Loop to keep app running
while running:
    ui.header("=== Main menu ===")
    print("""\n1. Add Transaction
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
        view_balance(transactions)
    elif user_input == 3:
        view_reports(transactions)
    elif user_input == 4:
        ui.header("=== App closed ===")
        running = False
    else:
        print("\nInvalid option.\n")
