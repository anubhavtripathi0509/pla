# Find how many times an array is rotated 

def count_rotation(arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        if arr[low] <= arr[high]:
            return low
        mid = low + (high - low) // 2
        next_ = (mid + 1) % len(arr)
        prev = (mid + len(arr) - 1) % len(arr)
        if arr[mid] <= arr[next_] and arr[mid] <= arr[prev]:
            return mid
        elif arr[mid] <= arr[high]:
            high = mid - 1
        elif arr[mid] >= arr[low]:
            low = mid + 1
    return -1

arr = [15, 18, 2, 3, 6, 12]
print(count_rotation(arr)) # 2
arr = [7, 9, 11, 12, 5]
print(count_rotation(arr)) # 4