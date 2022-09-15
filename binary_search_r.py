def binarySearch (array, x, low, high):
    if low <= high:

        mid = low + (high - low) // 2

        if x == array[mid]:
            return mid
        elif array[mid] > x:
            return binarySearch (array, x, low, mid-1)
        else:
            return binarySearch (array, x, mid+1, high)
    return -1

array = [3,4,5,6,7,8,9]
x = 8
result = binarySearch (array, x, 0, len(array) - 1)
if result != -1:
    print("Element found at index: " + str(result))
else:
    print("Element not found")