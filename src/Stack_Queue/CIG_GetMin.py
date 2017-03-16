stack = []
minStack = []


def pop():
    stack.pop()
    minStack.pop()


def push(data):
    stack.append(data)

    if len(minStack) == 0:
        minStack.append(data)
    else:
        propData = minStack[len(minStack) - 1]
        propData = data if propData > data else propData
        minStack.append(propData)


def clear():
    for _ in range(len(stack)):
        pop()


def getMin():
    return minStack[len(minStack) - 1]
