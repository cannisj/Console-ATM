# |>>> Taversh <<<| #


# Making an ATM Test 1 #


from os import system

# System("CLS") To clear the Output after an input or on to the next operation #

balance = 10000000

name = input("Who Is Making Use Of This ATM?\n")
system("CLS")
bank_name = "Access Bank\nZenith Bank\nEcoBank\nFidelity Bank"
Bank = input("What Bank Would you like to Access?\n")
system("CLS")

print("Welcome " + name + " To " + Bank + " Bank PLC")
print("""
1.Withdrawal
2.Transfer
3.Bill Payment
4.Balance Check
5.Support
""")
decision = str(input("How may I Help You? \n"))
system("CLS")
# If statements used for the decisions #
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
    else:
        print("Sorry You're not allowed here")
        exit()
        # exit() functions used to exit the program if pin is incorrect #

        # Transfer #
if decision == "2":
    print("Input four digit PIN Please ")
    pin = input()
    system("CLS")
    if pin == "0000":
        print("How much would you like to transfer?\n")
        trans_fer = int(input())
        system("cls")
        acct_num = int(input("Enter Account number\n"))
        system("cls")
        trans_ded = balance - trans_fer
        print(name + " You Have Transferred " + str(trans_fer) + " To " + str(
            acct_num) + "\nYour new Account Balance is: $" + str(trans_ded))
    else:
        print("Sorry You're not allowed here")
        exit()
        # Bill Payment #
if decision == "3":
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
                print(name + " The Payment of $" + str(debt) + " To " + str(acct_num) + " Was Successful,\n$" + str(
                    Payment) + " Is your new Account Balance")

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
                    print(name + " $" + str(credit_withdrawal) + " Has been sent to " + str(rec_num) + ", \n$" + str(
                        credit) + " Is your new Account Balance")
            else:
                rec_num = int(input("Recipient Number:\n"))
                system("CLS")
                if rec_num < 11:
                    print("Invalid Number")
                else:
                    credit_withdrawal = input("How much would you like to Buy?\n")
                    system("CLS")
                    credit = balance - int(credit_withdrawal)
                    print(name + " $" + str(credit_withdrawal) + " Has been sent to " + str(rec_num) + ", \n$" + str(
                        credit) + " Is your new Account Balance")
        if bill == "3":
            print("How many NEPA Points do you want to Buy?")
            nepa_points = input()

    else:
        print("Sorry You're not allowed here")
        exit()
        # Balance Check #
if decision == "4":
    print("Input four digit PIN Please ")
    pin = input()
    system("CLS")
    if pin == "0000":
        print(name + " Your balance is: $" + str(balance))
    else:
        print("Sorry You're not allowed here")
        exit()
        # Support #
if decision == "5":
    print("Input four digit PIN Please")
    pin = input()
    system("CLS")
    if pin == "0000":
        print(name + " We Will have you communicate with an official soon...")

        complaint = input(" What seems to be the issue? ")
    else:
        print("Sorry You're not allowed here")
        exit()

# //////////////    ////////////// #
#      ///               ///       #
#     ///               ///        #
#    ///          \\\  ///         #
#   ///       O    \\\///          #
