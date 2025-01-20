# Check if the array is sorted

def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

arr = [1, 2, 3,4, 5]
print(is_sorted(arr))