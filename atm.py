while True:
    Id = str(input("(Enter your id:"))
    if Id == 'Aditya':
        print
    balance = 10000
    print("  ATM  ")
    print("""
    1) balance
    2) withdraw
    3) deposit
    4)quit
    """)
    try:
        Option = int(input("Enter Option:"))
    except Exception as e:
        print("Error:404 not found", e)
        print("Please Enter 1,2,3,4 options only")
        continue
    if Option == 1:
        print("Your balance is:",balance)
    if Option ==2:
        print("Your balance is:", balance)
        Withdraw = float(input("Enter the amount of withdrawl: "))
        if balance < Withdraw:
            print("no balance")
        if Withdraw > 0:
            forwardbalance = (balance - Withdraw)
            print("remaining balance is:", forwardbalance)
        elif Withdraw > balance:
            print("no sufficient balance, sorry")
        else:
            print("no withdraw has been made")
    if Option == 3:
        print("your balance is:", balance)
        deposit = float(input("Enter the amount you want to deposit:"))
        if deposit > 0:
            forwardbalance = (deposit + balance)
            print("new balance is:", forwardbalance)
        elif deposit < 0:
            print("be serious buddy")
        else:
            print("no deposit has been made")
    if Option == 4:
        exit()








