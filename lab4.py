class Student:
    def __init__(self):
        self.age=0
        self.marks=0
        self.id=0
    def val_age(self):
            if self.age>20:
                return True
            else:
                return False
    def val_marks(self):
            if self.marks>=0 and self.marks<=100:
                return True
            else:
                return False
    def check_qualification(self):
            if self.val_age() and self.val_marks():
                if self.marks>=65:
                    return True
                else:
                    return False
            else:
                return False
    def setter(self):
            self.id=input("enter the id")
            self.age=int(input("Enter the age"))
            self.marks=int(input("Enter the marks"))
            
    def getter(self):
        x=self.check_qualification()
        if x:
                print(" id {} is ELIGIBLE to take admission".format(self.id))
        else:
                print("id {} is NOT_ELIGIBLE to take admission".format(self.id))

n=int(input("enter the number of students"))
for i in range(0,n):
    print(" student ",i+1," details")
    s=Student()
    s.setter()
    s.getter()
    

