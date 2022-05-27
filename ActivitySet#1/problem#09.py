
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
