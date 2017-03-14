import os


def show():
    parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(parentdir)


stack = []
minStack = []


def pop():
    stack.pop()
    minStack.pop()


def push(data):
    if len(minStack) == 0:
        minStack.append(data)
    else:
        temp = minStack.pop()
        minStack.append(temp)
        if temp > data:
            minStack.append(data)
        else:
            minStack.append(temp)
    stack.append(data)


def clear():
    for _ in range(len(stack)):
        pop()


def getMin():
    return minStack[len(minStack) - 1]
