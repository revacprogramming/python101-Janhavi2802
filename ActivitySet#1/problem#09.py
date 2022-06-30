
fname = input("Enter the file name: ")
try:
	fn = open(fname)
except:
        print("The file name doesn't exist")
        quit()
count = 0
total = 0
for line in fn:        	    
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        fline = line.find(':')
        num = line[fline+1:].strip()    
        S = float(num)
        total = total + S
average = total / count
print('Average spam confidence:', average)




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