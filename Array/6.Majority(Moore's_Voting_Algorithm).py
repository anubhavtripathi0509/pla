# Find majority element in an array (Moore's Voting Algorithm)
# Majority Element is an element that appears more than n/2 times in an array of size n.


from array import array


# brute force approach
def brute(a):
    for i in range(0, len(a)):
        count = 0
        for j in range(0, len(a)):
            if a[j] == a[i]:
                count += 1
        if count > len(a)/2:
            return a[i]


# Better Approach using hashmap
def better(a):
    hashmap = {}
    for i in range(0, len(a)):
        # print(hashmap)
        if a[i] in hashmap:
            # print(a[i], hashmap[a[i]])
            hashmap[a[i]] = hashmap[a[i]] + 1
        else:
            hashmap[a[i]] = 1
    
    for key, value in hashmap.items():
        # print(key, value)
        if value > len(a)/2:
            return key
        

# Optimal Approach using Moore's Voting Algorithm
def optimal(arr):
    count = 0
    element = 0
    for  i in range(0, len(arr)):
        if count == 0:
            element = arr[i]
        if arr[i] == element:
            count += 1
        
        else:
            count -= 1
    return element


arr = array('i', [2, 45, 2, 2, 31, 45, 2, 2, 2, 2, 10, 8, 2, 4])
print("Brute Force:", brute(arr))
print("Better Approach:", better(arr))
print("Optimal Approach:", optimal(arr))