import re

message="The current python virsion is 3.13"

# print("python"in message)
# print("134"in message)
# print(message.find("python"))

match_obj=re.search('13',message)

print(match_obj)

match_obj2=re.search("current",message)

print(match_obj2)

if re.search("virsion",message):
  print("found")
else:
  print("Not found")