print(end="Enter the size of the array: ")
tot = int(input())
arr = []
print(end = "Enter "+str(tot)+ " elements: ")
for i in range(tot):
    arr.append(input())

print(end= "\nEnter the value to delete: ")
val = input()

if val in arr:
    arr.remove(val)
    print("\nThe new array is: ")
    for i in range(tot-1):
        print(end=arr[i]+" ")
else:
    print("\nElement doesn't exist in the list!")