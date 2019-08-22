       #LAB-1.b----Fibonacci Series

nt=int(input("enter the number of terms in Fibonacci Series"))
n1=0
n2=1
c=0
if (nt<=0):
    print("Please enter the falid number of terms required")
elif(nt==1):
    print(n1)
else:
    print("Series is :")
    while(c<nt):
        print(n1,end="  ");
        nw=n1+n2
        n1=n2
        n2=nw
        c=c+1
