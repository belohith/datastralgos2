from collections import deque
stack = deque()
stack.append('s')
print(stack)
stack.append('u')
stack.append('v')
print(stack)
print(stack.pop())
print(stack)