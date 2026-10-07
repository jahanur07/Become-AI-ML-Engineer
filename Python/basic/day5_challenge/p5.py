def add_1(num):
  return num+1

def sqr(num):
  return num ** 2


num=int(input("Enter the number : "))
re1=add_1(num)
re2=sqr(re1)
print(f"the result is {re2}")