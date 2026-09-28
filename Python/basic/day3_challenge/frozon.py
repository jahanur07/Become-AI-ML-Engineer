s1=frozenset({2,3,1,2,1,3,4,5})
s2=frozenset({8,4,2,4,2,0,6,9})
operation1=s1 & s2
operation2=s1 | s2
operation3=s1 - s2
print(operation1, type(operation1))
print(operation2, type(operation2))
print(operation3, type(operation3))