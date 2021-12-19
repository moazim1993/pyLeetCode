"""
"""
stack = []
stack.append("First")
stack.append("Second")
stack.append("Third")
#LIFO
print("Stack : ", stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("Stack : ", stack)

queue = []
queue.append("First")
queue.append("Second")
queue.append("Third")
#FIFO
print("Queue : ", queue)
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("Queue : ", queue)
