# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:43:23 2021

@author: hongb
"""
def find_basins(bottom,board,length,height):
    searched = []
    frontier = [bottom]
    count = 1
    searched.append(bottom)
    while len(frontier) != 0:
        r,c = frontier.pop()
        
        if r != 0 and board[r-1][c] != 9 and (r-1,c) not in searched:
            frontier.append((r-1,c))
            searched.append((r-1,c))
            count += 1
        
            
    
        if r != height - 1 and board[r+1][c] != 9 and (r+1,c) not in searched:
           frontier.append((r+1,c))
           searched.append((r+1,c))
           count += 1
           
        if c != 0 and board[r][c-1] != 9 and (r,c-1) not in searched:
            frontier.append((r,c-1))
            searched.append((r,c-1))
            count += 1
        
            
    
        if c != length - 1 and board[r][c+1] != 9 and (r,c+1) not in searched:
           frontier.append((r,c+1))
           searched.append((r,c+1))
           count += 1
           
           
    return count
    
    
    

def get_risk(r,c,board, length, height):
    friends = []
    
    val = board[r][c]

    
    
    if r != 0:
        if board[r-1][c] <= val:
            return 0
    if r != height - 1:
        if board[r+1][c] <= val:
            return 0
        
    if c != 0:
        if board[r][c-1] <= val:
            return 0
        
    if c != length - 1:
        if board[r][c+1] <= val:
            return 0
    return val + 1
    
    
    
    
values = [i.strip().split() for i in open("input.txt", "r")]



board = []
for line in values:
    tmp = []
    for char in line[0]:
        tmp.append(int(char))
    board.append(tmp)
    
length = len(board[0])
height = len(board)

r = 0
c = 0

risk = 0

basins_point = []

while r < height and c < length:
    tmp = get_risk(r,c,board,length,height)
    if tmp != 0:
        basins_point.append((r,c))
    risk += tmp
    if c == length - 1:
        r += 1
        c = 0
    else:
        c+=1
        
print(risk)
areas = []
counter = 0
for locations in basins_point:
    areas.append(find_basins(locations, board, length, height))
    print(counter)
    counter += 1
areas.sort()
print(areas[-1]*areas[-2]*areas[-3])
