def linear_search(arr, target):
    for elem in arr:
        if elem is target:
            return elem

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here

    return -1  # not found


nums = [6, 1, 5, 37, 55, 38, 12, 0, 98, 3, 4, 86, 8, 4, 66]
print(linear_search(nums, 120))
