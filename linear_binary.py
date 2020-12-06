# Giving list


# Initialiaze a function that takes in two parameter
def binary(arr, target):
    #Initialize the left pointer
    left = 0
    #Initialize the right pointer
    right = len(arr) - 1
    while left <= right:
        #Get the value of the mid point
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

arr = [-2, 3, 4, 7, 8, 9, 11, 13]
assert search(arr, 11) == 6


