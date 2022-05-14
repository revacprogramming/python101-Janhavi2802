# Functions

def computepay(h, r):
    if h > 40:
        P = 1.5 * r * (h - 40) + (40 *r)
    else:
        P = h * r
    return P
        
	

hours = input(" Enter hour:")
h = float(hours)
rphrs = input("Enter rate per hours:")
rph = float(rphrs)

P = computepay(h,rph)
print("Pay",P)
