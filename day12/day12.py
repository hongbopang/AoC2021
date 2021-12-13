# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 13:54:12 2021

@author: hongb
"""
from time import time

values = [i.strip().split("-") for i in open("input.txt", "r")]

nodes = dict()

for line in values:
    start,end = line
    if start not in nodes:
        nodes[start] = []
    if end not in nodes:
        nodes[end] = []
        
    nodes[start].append(end)
    nodes[end].append(start)
    
start = time()
path_count = 0

frontier = [["start"]]

while len(frontier) != 0:

    me = frontier.pop()
    curr_pos = me[-1]
    if curr_pos == "end":
        path_count += 1
        continue
    neighbours = nodes[curr_pos]    
    for node in neighbours:
        if node.isupper() or node not in me:
            new_path = [i for i in me] + [node]
            frontier.append(new_path)
            
print(path_count)
end = time()
print(end-start)
path_count_2 = 0

frontier = [(["start"], True)]
start = time()
counter = 0
while len(frontier) != 0:
    curr = frontier.pop()
    me, small = curr
    
    curr_pos = me[-1]
    if curr_pos == "end":
        path_count_2 += 1
        continue
    neighbours = nodes[curr_pos]    
    for node in neighbours:
        if node == 'start':
            continue
        elif node.isupper() or node not in me:
            new_path = [i for i in me] + [node] 
            frontier.append((new_path, small))
            counter += 1
        if not node.isupper() and node in me and small:
            new_path = [i for i in me] + [node] 
            frontier.append((new_path, False))
            counter += 1
print(counter)
end = time()
print(end-start)          
print(path_count_2)