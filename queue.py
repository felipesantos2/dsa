# FILAS, QUEUES
# FIFO- First in, First Out
# LIFO - Last in First out

# [1, 2, 4]
# [4, 2, 1]

# Stack - LIFO Last In First Out
# 
stack = ["Felipe"]
def enqueue(data) -> list:
    stack.append(data)
    return stack

def dequeue(data) -> list:
    stack.pop()
    return data

enqueue("Pinheiro")
enqueue("dos")

print(enqueue("Santos"))
print(dequeue(stack))
