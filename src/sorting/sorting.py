# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Your code here
    # indices of a & b to track
    aIndex = 0
    bIndex = 0

    # for loop will check if we're at the end of arrA
    for i in range(len(merged_arr)):
        #if at the end of the a arr (edge case of arrA finished)
        if aIndex > len(arrA) - 1:
            #since no more elements in arrA, add rest of arrB elements
            merged_arr[i] = arrB[bIndex]
            bIndex += 1
        #elif check if at end of arrB (edge case fo arrB finished)
        elif bIndex > len(arrB) - 1:
            #since no more elemtns in arrB, add rest of arrA elemtns
            merged_arr[i] = arrA[aIndex]
            aIndex += 1
        # else (when not tat the end of either array, this is the main fn)
        else:
            # check which element is smaller and append it to the merged array
            if arrA[aIndex] > arrB[bIndex]:
                merged_arr[i] = arrB[bIndex]
                bIndex += 1
            else:
                merged_arr[i] = arrA[aIndex]
                aIndex += 1




    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    #split into 2 down midpointish
    midpoint = len(arr) // 2

    #assign left & right
    left = arr[:midpoint]
    right = arr[midpoint:]

    #break it down into all the individual elements, lots of left and rights
    #if len of left > 1, recurse
    if len(left) > 1:
        left = merge_sort(left)
    #if len of right > 1, recurse
    if len(right) > 1:
        right = merge_sort(right)

    # magically assume there's simultaneousl 5million  lefts and rights that will all merge at by calling merge once.
    # call merge()
        #to compare [] vs[], & join 'em back
    arr = merge(left, right)

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

