#non void functions

def add():
    return a+b
    
def sub():
    return a-b
    
def mul():
    return a*b
    
a = int(input("Enter the num a is :"))
b = int(input("Enter the num b is :"))

sums = add()
subs = sub()
muls = mul()

print(sums,subs,muls)

'''Enter the num a is :34
Enter the num b is :55
89 -21 1870

=== Code Execution Successful ==='''
