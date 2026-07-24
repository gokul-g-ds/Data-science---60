#global variable
print("Global")
def global_var():
    sum = a+b
    print(sum)
    
a = int(input())
b = int(input())

print("we not give input in fuction it get input from global : the ans is : ")
global_var()
print("global output : ",a+b)

'''Global
4
7
we not give input in fuction it get input from global : the ans is : 
11
global output :  11

=== Code Execution Successful ==='''

