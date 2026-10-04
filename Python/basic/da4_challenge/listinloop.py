countries=["India","united states","Australia","Ierland","Sri lanka","Iceland","Cuba","Iran","Poland"]
count=0
output=[]
for country in countries:
  # if country[0]=='I':
  if country.startswith('I'):
    count+=1
    output.append(country)

print(count)
print(output)