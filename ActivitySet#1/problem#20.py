count = 0
tot = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        count = count + 1
        num = float(line[21:]) #21 is the position  we find 0 in the lines starting with X-DSPAM:
        tot = num + tot
        avg = tot/count
print("Average spam confidence:",avg)