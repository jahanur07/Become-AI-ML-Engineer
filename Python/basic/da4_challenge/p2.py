sq=[2,4,1,33,1,122,1,9,2]
total=0
#using loop to calculate all value sum
for i in sq:
  total+=i
  print(i)
print(f"total is {total}")

#using sum function

sum1=sum(sq)
print(f"using function {sum1}")