# Object Oriented Programming
# https://www.py4e.com/lessons/Objects
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
d =dict()
for line in handle:
    if not line.startswith("from"):
       continue
    else:
        line = line.split()
        line=line[5]
        line=line[0:2]
        d[line]=d.get(lin

        
lst = list()
for value,count in d.items():
    lst.append(values,count) 
lat.sort()
for value,count in lst:
    print(value,count)