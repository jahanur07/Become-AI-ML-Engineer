import random
print("Welcome to the game !! ")

while True:
  choice=input("press 'enter' roll the dice and press 'q' to quit the game : ")
  choice=choice.strip()
  if choice=='q':
    print("thanks for playing the game , bye !!")
    break
  elif choice=='':
    number=random.randint(1,6)
    print(f"your number is {number}")
  else:
    print("Invalid Input")

print("The game is over !!")