def check_balance():
  print(f"Your current balance is {balance}")

def deposit(amount):
  global balance
  if amount >0:
    balance +=  amount 
  else:
    print("cannot deposit a negetive amount or zero amount ")
    
    
def withdraw(amount):
  global balance
  if amount <0 :
    print("cannot deposit a negetive amount or zero amount ")
  elif amount > balance:
    print("cannot withdraw , insufficient balance")
  else:
    balance -=amount
    

balance = 0.0

print("Wellcome to ABC bank !!")
while True:
  print("1. check you balance :")
  print("2. deposit an amount :")
  print("Withdraw an amount :")
  print("Quit")
  choice=int(input("Enter you choice (1-4):"))
  
  if choice==1:
    check_balance()
  elif choice == 2:
    amt=float(input("Enter deposit amount :"))
    deposit(amt)
  elif choice == 3:
    amt=float(input("Enter withdraw amount :"))
    withdraw(amt)
  elif choice == 4:
    break
  else:
    print("Invalid choice !!! Re-try !! ")
    
    
print("Thank you for banking with us ")