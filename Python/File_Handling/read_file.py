file_handler = open("practice.txt",'rt') #rt is the read mode 

#read operation
#content=file_handler.read() #this reads first 10 characters 

#readline()
# line1 = content=file_handler.readline()
# line2 = content=file_handler.readline()
# line3 = content=file_handler.readline()

lines = content=file_handler.readlines()

file_handler.close( )
# print(f"Line 1 : {line1}")
# print(f"Line 2 : {line2}")
# print(f"Line 3 : {line3}")


print(f"Lines : {lines}")
print(type(lines))

for line in lines:
  print(line.rstrip('\n'))
