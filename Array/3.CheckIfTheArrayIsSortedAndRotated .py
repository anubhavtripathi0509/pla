# Check if the array is sorted and rotated 

def is_sorted_and_rotated(arr):
    n = len(arr)
    min_index = 0
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            min_index = i
            break
    if min_index == 0:
        return False
    for i in range(1, n):
        if arr[(i + min_index) % n] < arr[(i + min_index - 1) % n]:
            return False
    return True