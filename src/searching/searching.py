def linear_search(arr, target):
    # Your code here
    if target in arr:
        return arr.index(target)

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    # find the middle point/index
    left = 0
    right = len(arr) - 1
    if len(arr) == 0:
        return -1
    while left <= right:
        midpoint = (left + right) //2
        if arr[midpoint] == target:
            return midpoint
        if arr[midpoint] < target:
            left = midpoint
        else:
            right = midpoint

    return -1  # not found
