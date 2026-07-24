#positional argument

def area_of_rec (len,wid):
    aor = len*wid
    print(aor)
    
area_of_rec(2,5)

#keyword 

def students(name,age):
    print(name,age)
    
students(name = "gokul",age = '24')

#default

def sum(a,c,b = 3):
    sums = a+b+c
    print(sums)
    
a = int(input("a is :"))
c = int(input("c is :"))

sum(a,c)

'''10
gokul 24
a is :3
c is :5
11

=== Code Execution Successful ==='''
