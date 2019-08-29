def fnum(l1,k):
    f=0
    n=len(l1)
    l=n-1
    while f<=l:
        m=int((f+l)/2)
        if(l1[m]==k):
            return 1
        elif(l1[m]<k):
            f=m+1
        else:
            l=l-1
    return 0
    
ele=int(input("enter the number of elements"))
olist=[]
print("Enter elements")
for i in range (0,ele):
        a=int(input())
        olist.append(a)
key=int(input("ENTER THE KEY"))
if(fnum(olist,key)):
        print("Number found")
else:
        print("Not found")
        
        
        
            
            
