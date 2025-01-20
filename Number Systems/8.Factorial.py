# Factorial of a number

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

n = int(input())
print(factorial(n))

# f=1
# for i in range(1,n+1):
#     f=f*i