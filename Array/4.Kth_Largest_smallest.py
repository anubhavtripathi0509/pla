#  K-th largest element in an array (e.g., 2nd, 3rd largest)

from array import array

def second_largest(arr):
    largest_arr = -1
    second_arr = -1
    for i in range(0, len(arr)):
        if arr[i] > largest_arr:
            largest_arr = arr[i]
        elif arr[i] < largest_arr and arr[i] > second_arr:
            second_arr = arr[i]

    return second_arr

arr = array('i', [12, 45, 2, 2, 31, 45,10, 8, 6, 4])

print("Second largest element is:", second_largest(arr))