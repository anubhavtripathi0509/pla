# Maximum and Minimum digit in a number

def max_min_digit(n):
    max_d = 0
    min_d = 9
    while n:
        r = n % 10
        max_d = max(max_d, r)
        min_d = min(min_d, r)
        n = n// 10
    return max_d, min_d

n = int(input())
max_d, min_d = max_min_digit(n)
print("Maximum digit:", max_d)
print("Minimum digit:", min_d)