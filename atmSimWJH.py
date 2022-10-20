#Name: Will Hurwitz
#Course: COMSC.230.01
#Prof. Name: Prof. Rivera
#Assignment (e.g. Homework # or Exam #): Mid-Term #1
#Program Name: atmSimWJH
#Program brief description: The program simulates the functions of an ATM.

account_number = 99999230
account_pin = 0o0230
checking_acc = 1000
savings_acc = 1000
num_of_tries = 0
transactionList = [] 
loop= True
a = """
1. Make a Deposit
2. Make a Withdrawal
3. Transfer balance
4. See balance
5. Exit 
"""



def userDeposit():
    global checking_acc, savings_acc
    che_or_sav = int(input('To deposit to your checkings account, enter 1. For your savings account, enter 2. '))
    amount_deposit = int(input('Enter the amount you would like to deposit (Must be greater than 0.): '))

    if che_or_sav == 1 and amount_deposit >= 0:
      checking_acc += amount_deposit
      print('New balance is: ', checking_acc)
      transactionList.append(che_or_sav)
      transactionList.append(amount_deposit)
      

    elif che_or_sav == 2 and amount_deposit >= 0:
        savings_acc += amount_deposit
        print('New balance is: ', savings_acc)
        transactionList.append(che_or_sav)
        transactionList.append(amount_deposit)




def userWithdrawal():
    global checking_acc, savings_acc
    che_or_sav = input('To deposit to your checkings account, enter 1. For your savings account, enter 2. ')
    amount_withdraw = input('Enter the amount you would like to withdraw: ')

    if che_or_sav == 1 and checking_acc >= amount_withdraw >= 0:
      checking_acc -= amount_withdraw
      print('New balance is: ', checking_acc)
      transactionList.append(che_or_sav)
      transactionList.append(amount_withdraw)
      

    elif che_or_sav == 2 and savings_acc >= amount_withdraw >= 0:
        savings_acc -= amount_withdraw
        print('New balance is: ', savings_acc)
        transactionList.append(che_or_sav)
        transactionList.append(amount_withdraw)
        



def userTransfer():
    global checking_acc, savings_acc
    che_or_sav = input('To transfer to your checkings account, enter 1. For your savings account, enter 2. ')
    amount_transfer = input('Enter the amount you would like to transfer: ')

    if che_or_sav == 1 and savings_acc >= amount_transfer >= 0:
        checking_acc += amount_transfer
        savings_acc -= amount_transfer
        print('New Checking Account Balance: ', checking_acc)
        print('New Savings Account Balance: ', savings_acc)
        transactionList.append(2)
        transactionList.append(2)
        transactionList.append(amount_transfer)
        transactionList.append(1)
        transactionList.append(1)
        transactionList.append(amount_transfer)

    elif che_or_sav == 2 and checking_acc >= amount_transfer >= 0:
        savings_acc += amount_transfer
        checking_acc -= amount_transfer
        print('New Savings Account Balance: ', savings_acc)
        print('New Checking Account Balance: ', checking_acc)
        transactionList.append(2)
        transactionList.append(1)
        transactionList.append(amount_transfer)
        transactionList.append(1)
        transactionList.append(2)
        transactionList.append(amount_transfer)



def seeBalance():
    che_or_sav = input('To see checkings account balance, enter 1. For your savings account balance, enter 2. ')
    if che_or_sav == 1:
        print('Checking Account Balance: ', checking_acc)
    elif che_or_sav == 2:
        print('Savings Account Balance: ', savings_acc)





while num_of_tries < 3:
    accnum = int(input('Enter Account Number: '))
    accpin = int(input('Enter Account Pin: '))

    if accnum == 99999230 and accpin == 0o0230:
        while(loop == True):
            num_of_tries = 3
            print(a)
            x = int(input('Enter the number that cooresponds to desired action: '))
            if x == 1:
                transactionList.append(1)
                userDeposit()
                

            elif x == 2:
                transactionList.append(2)
                userWithdrawal()
                

            elif x == 3:
                userTransfer()
            
        
            elif x == 4:
                seeBalance()

            elif x == 5:
                print('Your transaction receipt is listed below: ')
                new = []
                for i in range(0, len(transactionList), 3):
                    new.append(transactionList[i : i+3])
                print(new)
                print('Thank you. Goodbye. ')
                loop= False
                break



    else: 
        print('Access denied. Try again.')
        num_of_tries += 1
        if(num_of_tries == 3):
            print("Goodbye.")
            loop= False
            break 