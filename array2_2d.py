r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
two_arr = [ [0 for col in range(c)] for r in range(r)]

for row in range(r):
    for col in range(c):
        two_arr[row][col] = row*col
print(two_arr)