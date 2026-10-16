
while True:
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
        print("\nAdd Transaction selected...")
    elif user_input == 2:
        print("\nView Balance selected...")
    elif user_input == 3:
        print("\nView Reports selected...")
    elif user_input == 4:
        print("\n=== App closed ===")
        break
    else:
        print("\nInvalid option.\n")
    