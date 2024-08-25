# Console-ATM
This Program is a console ATM created with python with a fixed balance.

5-18-2024
Added a transaction history

8-10-2024
Updates
1. Another Transaction Feature
Description: A new feature has been added that prompts the user if they would like to perform another transaction after completing one. If the user selects "yes," the ATM menu restarts, allowing them to choose another operation. If the user selects "no," the program exits with a thank you message.
Usage: After completing any transaction, you will be asked:
Would you like to perform another transaction? (yes/no)
If "yes": The ATM menu will restart.
If "no": The program will exit.
2. Bug Fix: UnboundLocalError on Balance Calculation
Description: A bug was fixed where the application would raise an UnboundLocalError during a withdrawal operation. This error occurred because the balance variable was not correctly referenced within the atm_menu() function. The issue was resolved by declaring balance as a global variable.
Technical Details:
Added global balance inside the atm_menu() function to ensure that the global balance variable is updated correctly after each transaction.

8-24-2024
Added a change pin option