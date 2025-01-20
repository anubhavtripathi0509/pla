# Prime numbers in a given range

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def prime_range(start, end):
    for i in range(start, end+1):
        if is_prime(i):
            print(i)

start = 10
end = 50

prime_range(start, end)