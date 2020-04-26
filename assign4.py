# 1
for i, j in enumerate(A):
    A[i] = j[:-1]+(100,)

# 2
for i, j in enumerate(A):
    if not j:
        A.pop(i)
# 3
A.sort(reverse=True, key=lambda a: a[1])

# 4
count = 0
for i in A:
    if type(A) == tuple:
        break
    count += 1
# 5
 A.sort(reverse=True, key= lambda a:a[1])

# 6
from collections import defaultdict
d = defaultdict (set)
for i in range(len(A)):
    d[A[i]].add(B[i])

# 7
for i in d:
    d[i] = sum(d[i])
# 8
maxi = max(s)
mini = min(s)

# 9
ans = len(s)

# 10
ans = s-set(list)
