


def comp(k):
    if k=='(':
        return ')' 
    if k=='{':
        return '}'
    if k=='[':
        return ']'


def validate(s):
    l=[]
    top=-1
    for i in s:
        if len(l)==0 and i in ("{","(","["): 
           top=top+1
           l.append(i)
        x=comp(l[top])
        if len(l)!=0 and (i==x or (i in ("(","{","["))):
              if i==x:
                  l.pop()
                  top=top-1
              elif i in ("(","{","["):
                top=top+1
                l.append(i)
        else:
            print("Invalid")
    if len(l)==0:
        print("Valid")
string=input("enter the string")
validate(string)
