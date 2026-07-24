print("Recursive Function")

#sum of numbers 

def SON(n):
    if(n == 1):
      return 1
    
    return n + SON(n-1)
    
n = int(input())
print("Enter the num is : ",n)
result = SON(n)
print(result)

'''Recursive Function
7
Enter the num is :  7
28

=== Code Execution Successful ==='''
