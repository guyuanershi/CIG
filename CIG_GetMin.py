
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


def getMin():
    return minStack[len(minStack) - 1]


if __name__ == '__main__':
    push(13)
    push(5)
    push(40)
    push(10)
    push(6)
    push(19)
    push(2)
    push(8)

    print(getMin())
    pop()
    pop()
    pop()

    print(getMin())
