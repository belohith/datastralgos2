def insertionSortA(array):
    for step in range(1,len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j - 1
        array[j + 1] = key

def insertionSortD(array):
    for step in range(1,len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key > array[j]:
            array[j+1] = array[j]
            j = j - 1
        array[j + 1] = key

data = [5,2,1,7,8]
insertionSortA(data)
print('Sorted Array in Ascending Order: ')
print(data)
insertionSortD(data)
print('Sorted Array in Descending Order: ')
print(data)