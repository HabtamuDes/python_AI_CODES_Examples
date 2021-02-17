import re

hand = open("/home/warcraft/regx_sum_172486.txt")
a=list()
for line in hand:
     b = re.findall('[0-9]+',line)
     a = a+b

sum = 0
for c in a:
    sum = sum + int(c)

print(sum)

