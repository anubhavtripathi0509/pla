# Check if a number is palindrome or not

def is_palindrome(num):
    return str(num) == str(num)[::-1]

num = 121
print(is_palindrome(num))


# Without using string
def no_str_is_palindrome(num):
    temp = num
    rev = 0
    while num > 0:
        d = num%10
        rev = rev*10 + d
        num = num // 10
    return temp == rev

num = 121
print(no_str_is_palindrome(num))