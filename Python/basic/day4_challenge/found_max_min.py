# sq=[2,4,1,33,1,122,1,9,2]

# highest=sq[0]
# #founding max value using loop for go every index 
# for i in sq:
#   if highest < i:
#     highest=i

# print(f"highest value is {highest}")
# #using max function
# max1=max(sq)
# print(max1)

sq=[2,4,1,33,1,122,1,9,2]

lowest=sq[0]
#founding min value using loop for go every index 
for i in sq:
  if lowest > i:
    lowest=i

print(f"highest value is {lowest}")
#using min function
min1=min(sq)
print(min1)