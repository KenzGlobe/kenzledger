
import json

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
        