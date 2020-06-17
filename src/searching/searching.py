# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    if start < end:
        mid = (end + start) // 2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            return binary_search(arr, target, mid + 1, end)
        elif target < arr[mid]:
            return binary_search(arr, target, start, mid)
        else:
            return -1
    else:
        return -1





# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively




