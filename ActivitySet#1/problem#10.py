fname = input("Enter file name: ")
fh=open(fhname)
lst = list()
for line in fh:
  line.rstrip()
for line in fh:
    for word in line.split():
        if not word in lst:
            lst.append(word)
    lst.sort()
print(lst)

