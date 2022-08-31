from queue import LifoQueue
stack = LifoQueue(maxsize=3)
stack.put('w')
stack.put('x')
stack.put('y')
print(stack.qsize())
print(stack.full())
stack.get()
print(stack.full())