class CallDetail(object):
    def __init__(self):
         self.caller=None
         self.called=None
         self.duration=None
         self.type_of_call=None
class Util:
    def __init__(self):
         self.list_of_call_objects=None
    def parse_customer(self,list_of_call_string):
        l=[]
        for i in range(0,3):
            l.append(CallDetail())
        for i in range(0,3):
            l[i]=list_of_call_string[i]
        self.list_of_call_objects=l
        '''for i in self.list_of_call_objects:
            print(i)'''
    def view(self,num):
        tl=self.list_of_call_objects[num].split(",")
        print("caller:",tl[0])
        print("called:",tl[1])
        print("duration:",tl[2])
        print("Type:",tl[3])
        
call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'
list_of_call_string=[call,call2,call3]
obj=Util()
obj.parse_customer(list_of_call_string)
print("Enter the object number to see its detail")
n=int(input())
obj.view(n-1)
