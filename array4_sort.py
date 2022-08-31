arr = [10, 22, 34, 12, 66]
temp = 0

print("Elements of original array: ")
for i in range(0, len(arr)):
    print(arr[i])

for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if(arr[i] > arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp;
print();

print("Elements of the sorted new array ascending: ")
for i in range(0, len(arr)):
    print(arr[i])
