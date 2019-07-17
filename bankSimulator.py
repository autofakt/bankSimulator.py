'''
Programmer:
Description: A program called BankApp to simulate a banking application.
Date: 07/13/2019
'''

file = open('userInfo.txt','r')  # Open userinfo txt file to read data

userName = []   # Three lists to keep the vital data
password = []
balance = []

def printHeader():
   print('==========================')
   print('      Bank of America')
   print('==========================')
   
def login():       # Function to login return -1 if no match, otherwise returns index number in list
   inputUserName = input('Enter username: ')      # to use as customer ID.
   inputPassword = input('Enter password: ')
   for users in userName:   
      if users == inputUserName:        # checks if user is in the list
         index = userName.index(inputUserName)      # if user found extracts index number
         if inputPassword == password[index]:        # uses index to check if the password matches
            return index         # return index if login is a match
   return -1         # returns -1 if no match found
   
def printMenu():  # Main menu
   print('--------------------------')
   print('         Menu')
   print('--------------------------')
   print('Type D to deposit money')
   print('Type W to withdraw money')
   print('Type B to display balance')
   print('Type C to change user, display username')
   print('Type E to exit')
   option = input('Enter selection: ').upper()
   return option
   
def deposit(amount):
   balance[customerID] += round(amount,2)
   showBalance()
    
def withdraw(amount):
   while amount > balance[customerID]:  # Error checking to stop overdraft
      print('Cannot withdraw more than you have')
      amount = float(input("Enter amount to withdraw: "))
   balance[customerID] -= round(amount,2)
   showBalance()
    
def showBalance():
   print('Balance: ', round(balance[customerID],2))
   
def exit():
   exit = open('userInfo.txt', 'w')  # Opens the data file to overwrite the old balances
   for y in range(len(userName)):
         exit.write(userName[y] +'\t' + password[y] +'\t' + str(round(balance[y],2))+'\n')

for i in file:    # loads userInfo.txt in each list
   line = i.split()
   userName.append(line[0])
   password.append(line[1])
   balance.append(float(line[2]))

printHeader()  # Prints Bank of America text
customerID = login()  # Assigns ID number to each client, uses index from list as ID
option = 'P'  # Default option

while customerID == -1:  # If customer ID is -1 that means it was not found and makes you re-enter
   print('Invalid login, try again')
   customerID = login()
while customerID >-1 and option != 'E':  #If customer ID found and option Exit is not set menu shows
   option = printMenu()
  
   if option == 'D':
      print('--------------------------')
      print('         Deposit')
      print('--------------------------')
      amount = float(input("Enter amount to deposit: "))
      deposit(amount)
      
   if option == 'W':
      print('--------------------------')
      print('         Withdraw')
      print('--------------------------')
      showBalance()
      amount = float(input("Enter amount to withdraw: "))
      withdraw(amount)
      
   if option == 'B':
      print('--------------------------')
      print('         Balance')
      print('--------------------------')
      showBalance()
      
   if option == 'C':
      print('--------------------------')
      print('         Change User')
      print('--------------------------')
      customerID = login()
      while customerID == -1:
         print('Invalid login, try again')
         customerID = login()
         
   if option == 'E':
      print('==========================')
      print('         Exit')
      print('==========================')
      exit()
