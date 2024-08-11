# |>>> Taversh <<<| #


# Making an ATM Test 1 #


from os import system

balance = 10000000
transaction_history = []  # Empty list used to store transaction history

name = input("Who Is Making Use Of This ATM?\n")
system("CLS")
bank_name = "Access Bank\nZenith Bank\nEcoBank\nFidelity Bank"
Bank = input("What Bank Would you like to Access?\n")
system("CLS")

def atm_menu():
    global balance # Declare balance as a global variable
    
    print("Welcome " + name + " To " + Bank + " Bank PLC")
    print("""
    1.Withdrawal
    2.Transfer
    3.Bill Payment
    4.Balance Check
    5.Support
    6.Deposit
    7. Mini Statement  # New option added
    """)
    decision = str(input("How may I Help You? \n"))
    system("CLS")
    
    # Withdrawal #
    if decision == "1":
        print("Input four digit PIN please")
        pin = input()
        system("CLS")
        if pin == "0000":
            print("How Much would you like to withdraw?")
            print("Your Bank Charge Depends on your Amount")
            withdrawal = int(input())
            system("CLS")
            if withdrawal < 10000:
                charges = 10.34
            if withdrawal > 10000:
                charges = 23.41
            if withdrawal >= 20000:
                charges = 41.99
            # Every charge set is different due to the range of money withdrawn #
            Total = balance - withdrawal - charges
            print("$" + str(withdrawal) + " Has been withdrawn.\nTotal is: $" + str(Total))
            transaction_history.append(f"Withdrawal: -${withdrawal}")  # Record withdrawal
        else:
            print("Sorry You're not allowed here")
            exit()
    
    # Transfer #
    elif decision == "2":
        print("Input four digit PIN Please ")
        pin = input()
        system("CLS")
        if pin == "0000":
            print("How much would you like to transfer?\n")
            trans_fer = int(input())
            system("CLS")
            acct_num = int(input("Enter Account number\n"))
            system("CLS")
            trans_ded = balance - trans_fer
            print(name + " You Have Transferred " + str(trans_fer) + " To " + str(acct_num) + "\nYour new Account Balance is: $" + str(trans_ded))
            transaction_history.append(f"Transfer: -${trans_fer}") # Record transfer
        else:
            print("Sorry You're not allowed here")
            exit()
    
    # Bill Payment #
    elif decision == "3":
        print("Input four digit PIN Please ")
        pin = input()
        system("CLS")
        if pin == "0000":
            print("What Bill do you want to pay?\n")
            bill = input("1.House Rent\n2.Airtime\n3.NEPA points\n")
            system("CLS")
            if bill == "1":
                print("How Much do you need to Pay?")
                debt = int(input())
                system("CLS")
                acct_num = int(input("Landlord Account number\n"))
                system("CLS")
                Payment = balance - debt
                if acct_num < 10:
                    print("Invalid Account Number")
                else:
                    print(name + " The Payment of $" + str(debt) + " To " + str(acct_num) + " Was Successful,\n$" + str(Payment) + " Is your new Account Balance")
                    transaction_history.append(f"Bill Payment: -${debt}") # Record bill payment
            if bill == "2":
                airtime = input("For Self or Others?\n")
                system("CLS")
                if airtime == "Self":
                    rec_num = int(input("Your Number:\n"))
                    system("CLS")
                    if rec_num < 11:
                        print("Invalid number")
                    else:
                        credit_withdrawal = input("How much would you like to Buy?\n")
                        system("CLS")
                        credit = balance - int(credit_withdrawal)
                        print(name + " $" + str(credit_withdrawal) + " Has been sent to " + str(rec_num) + ", \n$" + str(credit) + " Is your new Account Balance")
                        transaction_history.append(f"Airtime (Self): -${credit_withdrawal}")
                else:
                    rec_num = int(input("Recipient Number:\n"))
                    system("CLS")
                    if rec_num < 11:
                        print("Invalid Number")
                    else:
                        credit_withdrawal = input("How much would you like to Buy?\n")
                        system("CLS")
                        credit = balance - int(credit_withdrawal)
                        print(name + " $" + str(credit_withdrawal) + " Has been sent to " + str(rec_num) + ", \n$" + str(credit) + " Is your new Account Balance")
                        transaction_history.append(f"Airtime (Others): -${credit_withdrawal}") 
            if bill == "3":
                print("How many NEPA Points do you want to Buy?")
                nepa_points = input()
    
        else:
            print("Sorry You're not allowed here")
            exit()
    
    # Balance Check #
    elif decision == "4":
        print("Input four digit PIN Please ")
        pin = input()
        system("CLS")
        if pin == "0000":
            print(name + " Your balance is: $" + str(balance))
        else:
            print("Sorry You're not allowed here")
            exit()
    
    # Support #
    elif decision == "5":
        print("Input four digit PIN Please")
        pin = input()
        system("CLS")
        if pin == "0000":
            print(name + " We Will have you communicate with an official soon...")
    
            complaint = input(" What seems to be the issue? ")
        else:
            print("Sorry You're not allowed here")
            exit()
    
    # Deposit #
    elif decision == "6":
        print("Input four digit PIN please")
        pin = input()
        system("CLS")
        if pin == "0000":
            deposit_amount = int(input("How much would you like to deposit?\n"))
            system("CLS")
            balance = balance + deposit_amount
            print("$", deposit_amount, "Has been deposited.\nYour new balance is: $", balance)
            transaction_history.append(f"Deposit: +${deposit_amount}")  # Record deposit
        else:
            print("Sorry You're not allowed here")
            exit()
    
    # Mini Statement #
    elif decision == "7":  # New option for Mini Statement
        print("\nMini Statement:")
        if transaction_history:
            for transaction in transaction_history[-3:]:
                print(transaction)
        else:
            print("No recent transactions.")
    
    else:
        print("Invalid selection. Exiting.")
        exit()

    # Ask if the user wants to perform another transaction
    another_transaction = input("Would you like to perform another transaction? (yes/no)\n").lower()
    system("CLS")
    if another_transaction == "yes":
        atm_menu()  # Restart the ATM menu
    else:
        print("Thank you for using the ATM. Goodbye!")
        exit()

# Start the ATM program
atm_menu()

# //////////////    ////////////// #
#      ///               ///       #
#     ///               ///        #
#    ///          \\\  ///         #
#   ///       O    \\\///          #
