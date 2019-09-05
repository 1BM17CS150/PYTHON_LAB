n=int(input("Enter the to find its divisor"))
l=[]
for i in range(1,n+1):
    if(n%i==0):
        l.append(i)

print("Possible Divisors of {} are {}".format(n,l))
