def partition(arr, l, h):
    pivot = arr[h]
    i = l - 1

    for j in range(l, h):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i+1], arr[h]) = (arr[h], arr[i+1])

    return i+1

def quickSort(arr, l, h):
    if l < h:
        pi = partition(arr, l, h)
        quickSort(arr, l, pi - 1)
        quickSort(arr, pi + 1, h)
        
d = [9,8,7,2,10,20,1] 

print("Unsorted Array: ")
print(d)
size = len(d)
quickSort(d, 0, size - 1)
print("Sorted array in ascending order using quick sort: ")
print(d)