import re
h=open("regex_sum_42.txt")
l=list()
y=re.findall('[0-9]+',l)
print(y)
sum=0
for x in y:
    sum=sum+int(x)
print(sum)
