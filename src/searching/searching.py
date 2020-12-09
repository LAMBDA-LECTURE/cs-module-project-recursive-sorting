# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # find a midpoint
    #left & right pointers = start and end bc crazy
    #if targer is < midpoint, go left
        #recurse
    #elif taget == endpoint, return index

    # return target index
    # Check base case
    if end >= start:
        # print(arr)
        mid = (end + start) // 2

        # If element is present at the middle itself
        if arr[mid] == target:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, target, mid + 1, end)

    else:
        # Element is not present in the array
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    print("SORTED(ARR)", sorted(arr))
    if arr[0] < arr[-1]:
        return binary_search(arr, target, 0, len(arr)-1)
    else:
        reverseIndex = binary_search(sorted(arr), target, 0, len(arr)-1)
        if reverseIndex == -1:
            return -1
        return len(arr) - reverseIndex - 1
# testin testin juan

