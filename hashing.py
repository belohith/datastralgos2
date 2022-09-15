def hashing (k, m):
    return k % m

m = 8

print (f'The hash value for 4 is {hashing(4,m)}')
print (f'The hash value for 5 is {hashing(5,m)}')
print (f'The hash value for 10 is {hashing(10,m)}')
print (f'The hash value for 12 is {hashing(12,m)}')
print (f'The hash value for 8 is {hashing(8,m)}')