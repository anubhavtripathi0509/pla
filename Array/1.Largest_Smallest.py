#  Largest and smallest elements in an array

def largest_smallest(arr):
    sorted_arr = sorted(arr)
    return sorted_arr[-1], sorted_arr[0]

arr = [12, 45, 2, 41, 31, 10, 8, 6, 4]
print("Largest and smallest elements in an array: ", largest_smallest(arr))