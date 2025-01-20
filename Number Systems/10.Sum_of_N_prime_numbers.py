# Sum of the first N prime numbers

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def sum_of_primes(n):
    sum = 0
    i = 2
    count = 0
    while count < n:
        if is_prime(i):
            sum = sum + i
            count = count + 1
        i = i + 1
    return sum

n = int(input())
print(sum_of_primes(n))