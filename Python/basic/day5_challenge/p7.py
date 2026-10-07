l1=[3,2,1,3,21,2,3]

odd =filter(lambda x: True if x % 2 != 0 else False,l1)
print(list(odd))