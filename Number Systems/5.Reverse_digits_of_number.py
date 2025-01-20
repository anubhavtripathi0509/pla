# Reverse digits of a number

def reverse_digits(num):
    rev = 0
    while num >0:
        d = num%10
        rev = rev*10 + d
        num = num//10
    
    return rev

num = 12345
print(reverse_digits(num))