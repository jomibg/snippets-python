from collections import deque
dq=deque(range(5),maxlen=5)
print(dq)# 0,1,2,3,4
dq.rotate(1)
print(dq)# 4,0,1,2,3
dq.rotate(-2)
print(dq)# 1,2,3,4,0
dq.appendleft(-1)
print(dq)# -1,1,2,3,4
dq.extend([5,6])
print(dq)# 2,3,4,5,6
dq.popleft()
print(dq)# 3,4,5,6
