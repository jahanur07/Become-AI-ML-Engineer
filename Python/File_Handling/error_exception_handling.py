"""
1. Compile time Error => syntax error & indentation error
2. Exceptions => Error during execution
"""



try:
  a=int(input("Enter a number :"))
  b=int(input("Enter a number :"))  
  result=a/b
  print(result)
  
except ZeroDivisionError:
  print("Denominator should not be 0")
  
except ValueError:
  print("Input should be digit ")