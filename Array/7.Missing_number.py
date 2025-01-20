# Missing number 

def missing_number(arr):
    n = len(arr) + 1
    total = n * (n + 1) // 2
    return total - sum(arr)

def hash(arr):
    n = len(arr) + 1
    hash_table = [0] * n
    for i in arr:
        hash_table[i] = 1
    for i in range(1, n):
        if hash_table[i] == 0:
            return i

arr = [1, 2, 3, 4, 6, 7, 8]
print(missing_number(arr))