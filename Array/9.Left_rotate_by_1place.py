# Left rotate by one place

def left_rotate_by_one(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]
    arr[-1] = temp
    return arr

def left_rotate_by_d_places(arr, d):
    arr = arr[d:] + arr[:d]