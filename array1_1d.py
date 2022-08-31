print("How many elements inside the array?", end="")

num = input()
arr=[]
print("\nEnter", num, "elements:", end="")

num = int(num)

for i in range (num):
    element = input()
    arr.append(element)
print("\nThe elements in array are: ")
for i in range(num):
    print(arr[i]+" ", end="")