"""
Returns the index of x in the array if it's present, otherwise it returns -1
"""

def binary_search(arr, l, r, x):

    # Check base case
    if (r >= 1):
        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if (arr[mid] == x):
            return mid

        # If element is smaller than the middle, then it can only be present in the left subarray
        elif (arr[mid] > x):
            return binary_search(arr, l, mid-1, x)

        # Else - the element can only be present in the right subarray
        else:
            return binary_search(arr, mid+1, r, x)
    
    else:
        # Element is not present in the array
        return -1

# Test program
arr = [2, 3, 4, 10, 40]
x = 10

# Fucntion call
result = binary_search(arr, 0, len(arr)-1, x)

if result != 1:
    print("Element is present at index {}".format(result))
else:
    print("Element is not present in the array")