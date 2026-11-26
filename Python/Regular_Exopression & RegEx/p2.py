import re
s1="Python is a programming language python3.13 is the current virsion"

# pat= r"old\new"
# print(pat)

# pat=r"[a-z][a-z]"

# match_obj=re.search(pat,s1)
# print(match_obj)

#\d and \D
#\d match 1 digit charachter. it is similer to [0-9]

pat=r"[a-z][a-z][a-z]\d"

match_obj=re.search(pat,s1)
print(match_obj)

#\s , \S 
#\s match whitespace charachter. tab and new line charachter also

pat=r"[a-z][a-z][a-z]\s"

match_obj=re.search(pat,s1)
print(match_obj)

s2="""hello
everyone
we are learning pyhton
through tutedude specail thank you for 
tutedude management team
"""

pat=r"[a-z][a-z][a-z]\s"

match_obj=re.search(pat,s2)
print(match_obj)

#\S => opposite of \s.It match any charachter except space,\n and \t

pat=r"[a-z][a-z][a-z]\S"

match_obj=re.search(pat,s2)
print(match_obj)