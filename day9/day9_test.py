# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 13:37:04 2021

@author: hongb
"""


# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 13:35:47 2021

@author: hongb
"""


import time
x = []
with open("input.txt") as f:
    for i in f.readlines():
        x.append(i[:-1])
ans = []
for i in range(len(x)):
    c = []
    for j in x[i]:
        c.append(int(j))
    x[i] = c
start = time.time()
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def dfs(i, j, currsize, seen):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for k in dirs:
        ni, nj = i + k[0], j + k[1]
        if 0 <= ni < len(x) and 0 <= nj < len(x[0]) and x[ni][nj] > x[i][j] and x[ni][nj] != 9 and (ni, nj) not in seen:
            seen.add((ni, nj))
            currsize += dfs(ni, nj, 1, seen)
    return currsize

for i in range(len(x)):
    for j in range(len(x[i])):
        AllSmall = True
        for k in dirs:
            ni, nj = i + k[0], j + k[1]
            if 0 <= ni < len(x) and 0 <= nj < len(x[0]):
                if x[i][j] < x[ni][nj]:
                    AllSmall = True
                else:
                    AllSmall = False
                    break
        if AllSmall:
            ans.append(dfs(i, j, 1, set()))
ans = sorted(ans)
print(ans[-1] * ans[-2] * ans[-3])
print(time.time() - start)