def calculator(a,b):
  c=a+b
  d=a*b
  e=a//b
  
  return c,d,e


a=int(input("Enter the number a : "))
b=int(input("Enter the number b : "))

rel1,rel2,rel3=calculator(a,b)
print(f"the Addition is {rel1}")
print(f"the multiplication is {rel2}")
print(f"the subtraction is {rel3}")