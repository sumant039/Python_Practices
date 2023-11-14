# # Python 3 program to find 
# # factorial of given number
# def factorial(n):
     
#     # single line to find factorial
    
#     if (n==1 or n==0):
#         return 1 
#     else: 
#         return n * factorial(n - 1) 
 
# # Driver Code
# n = 5
# print("Factorial of",n,"is",factorial(n))

# def factorial(n):
#     if (n==1 or n==0):
#         print(1)
#     else:
#         print(n* (factorial(n-1)))
# factorial(5)


def factorial(n):
     if (n==0 or n==1):
         return 1
     else:
         return n * factorial(n - 1)
n=5
print(factorial(n))