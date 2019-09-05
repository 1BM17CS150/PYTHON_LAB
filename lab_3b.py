import string
import random
def pass_gen(pl=10):
    password=[]
    p_char=string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation
    for i in range(pl):
        password.append(random.choice(p_char))
    return ''.join(password)
s=int(input("Enter the length of password you want. NOTE : length cannot be less than 5 \n "))

if(s<5):
    print("For strong PASSWORD length should  NOT be less than 5.")
    
else:
    print("password  is:",pass_gen(s))
    
    
    
