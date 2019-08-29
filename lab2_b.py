def rev(s):
     l1=s.split(" ")
     l2=l1.copy()
     l1.reverse()
     a1=" "
     s1=a1.join(l1)
     print(s1,"\n")
     print(s1[::-1])

s=input("enter the string")
rev(s)

