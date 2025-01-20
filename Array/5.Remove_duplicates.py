# Remove duplicates in an array

from array import array

def remove_duplicates(arr):
    unique_arr = []
    for i in range(0, len(arr)):
        if arr[i] not in unique_arr:
            unique_arr.append(arr[i])

    return unique_arr

# set brute force approach
def brute(arr):
    unique_set = set()
    for i in range(0, len(arr)):
       unique_set.add(arr[i])

    new_arr = array('i', unique_set)
    return new_arr

def better(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            arr[i+1] = arr[j]
            i = i+1
    return arr[:i+1]

arr = array('i', [12, 45, 2, 2, 31, 45,10, 8, 6, 4])
brute_arr = brute(arr)
better_arr = better(arr)
print("Brute Force:", brute_arr)
print("Better Approach:", better_arr)