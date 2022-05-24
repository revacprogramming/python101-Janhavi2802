# Files

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0

for line in fh:
    if not  line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count=count+1
        z=line.find('0')
        y=float(line[z:])
        total=total+y
asc=total/count             
        
print("Average spam confidence:",asc)
