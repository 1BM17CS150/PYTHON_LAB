

class validation:
    def comp(self,k):
        if k=='(':
            return ')' 
        if k=='{':
            return '}'
        if k=='[':
            return ']'


    def validate(self,s):
        l=[]
        top=-1
        for i in s:
            if len(l)==0 and i in ("{","(","["): 
               top=top+1
               l.append(i)

            elif len(l)!=0 and (i==self.comp(l[top]) or (i in ("(","{","["))):
                  if i==comp(l[top]):
                      l.pop()
                      top=top-1
                  elif i in ("(","{","["):
                    top=top+1
                    l.append(i)
            else:
                print("Invalid")
                return
        if len(l)==0:
            print("Valid")
        else:
            print("Invalid")
string=input("enter the string")
obj=validation()
obj.validate(string)
