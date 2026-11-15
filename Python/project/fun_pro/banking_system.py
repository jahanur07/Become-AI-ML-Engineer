def check_balance():
  pass

def deposit():
  pass

def withdraw():
  pass

balance = 0

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
    deposit()
  elif choice == 3:
    withdraw()
  elif choice == 4:
    break
  else:
    print("Invalid choice !!! Re-try !! ")
    
    
print("Thank you for banking with us ")