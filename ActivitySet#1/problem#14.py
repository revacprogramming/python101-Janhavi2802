# Using Web Services
# https://www.py4e.com/lessons/servces
import re
fh = input("Enter the file name:")
fhand = open(fh)
sum = 0
for line in fhand:
  num = re.findall("[0-9]+",line)
  length = len(num)
  for i in range(length):
     sum = sum + int(num[i])
print(sum)