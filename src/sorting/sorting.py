# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    i = 0
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] < arrB[0]:
            merged_arr[i] = arrA[0]
            del arrA[0]
        elif arrB[0] < arrA[0]:
            merged_arr[i] = arrB[0]
            del arrB[0]
        i += 1

    while len(arrA) > 0:
        merged_arr[i] = arrA[0]
        del arrA[0]
        i += 1

    while len(arrB) > 0:
        merged_arr[i] = arrB[0]
        del arrB[0]
        i += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        return merge(merge_sort(arr[: mid]), merge_sort(arr[mid:]))



    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

