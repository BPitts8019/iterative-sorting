def linear_search(arr, target):
    for cur_index in range(len(arr)):
        if arr[cur_index] == target:
            return cur_index

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    is_done = False
    start_index = 0
    end_index = len(arr)-1
    cur_index = (end_index - start_index) // 2

    while len(arr) > 0 and not is_done:
        if arr[cur_index] == target:
            return cur_index

        if cur_index >= end_index:
            is_done = True
        else:
            if arr[cur_index] < target:
                start_index = cur_index + 1
            else:
                end_index = cur_index - 1
            cur_index = ((end_index - start_index) // 2) + start_index

    return -1  # not found


nums = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
nums2 = []
print(binary_search(nums2, -6))
