def selectionSortA(array, size):
    for step in range(size):
        min = step
        for i in range(step + 1, size):
            if array[i] < array[min]:
                min = i
        (array[step], array[min]) = (array[min], array[step])

def selectionSortD(array, size):
    for step in range(size):
        min = step
        for i in range(step + 1, size):
            if array[i] > array[min]:
                min = i
        (array[step], array[min]) = (array[min], array[step])

data = [-20, 45, 12, 22, 19]
size = len(data)
selectionSortA(data, size)
print("Sorted array in ascending order: ")
print(data)
selectionSortD(data, size)
print("Sorted array in descending order: ")
print(data)