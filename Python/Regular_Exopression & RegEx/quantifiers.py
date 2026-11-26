import re
s1="""hello
everyone
we are learning pyhton
through tutedude specail thank you for 
tutedude management team
"""

pat=r"[a-z]{4}"
match_obj=re.search(pat,s1)
print(match_obj)