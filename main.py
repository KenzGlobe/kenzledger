"""
    KenzLedger
"""

# Imports
from storage import load_transactions as load_tx
from commands import add_transaction, view_balance, view_reports, delete_transaction
import kenz_ui as ui

# App Header
ui.big_title("KenzLedger")

# Variables
running = True

# Load transactions.json file
transactions = load_tx("transactions.json")

def app(transactions):
    global running
    
    while running:
        ui.header("=== Main menu ===")
        print("""\n1. Add Transaction
2. View Balance
3. View Reports
4. Delete Transaction
5. Exit\n""")
    
        try:
            user_input = int(input("===» Choose an option (1-5): "))
        except ValueError:
            print("\nInvalid input.\nPlease enter a number (1-5).")
            continue

        if user_input == 1:
            add_transaction(transactions)
        elif user_input == 2:
            view_balance(transactions)
        elif user_input == 3:
            view_reports(transactions)
        elif user_input == 4:
            delete_transaction(transactions)
        elif user_input == 5:
            ui.header("=== App closed ===")
            running = False
        else:
            print("\nInvalid option.\n")

if __name__ == "__main__":
    app(transactions)
