import sys
from collections import deque

number = int(sys.stdin.readline())
deq = deque([])

for i in range(number):
    q = sys.stdin.readline().split()

    command = q[0]

    if command == 'push':
        deq.append(q[1])
    elif command == 'pop':
        if not deq:
            print(-1)
        else:
            print(deq.popleft())
    elif command == 'front':
        if not deq:
            print(-1)
        else:
            print(deq[0])
    elif command == 'back':
        if not deq:
            print(-1)
        else:
            print(deq[-1])
    elif command == 'size':
        print(len(deq))
    elif command == 'empty':
        if not deq:
            print(1)
        else:
            print(0)