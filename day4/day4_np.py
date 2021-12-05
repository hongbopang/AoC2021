# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 16:59:11 2021

@author: hongb
"""

import numpy as np


class board:
    def __init__(self,values):
        self.board = np.zeros((5,5))
        self.locations = dict()

        r = 0
        for row in values:
            for c, value in enumerate(row.split()):
                self.locations[value] = (r,c)
            r += 1
        self.won = False
        

    def mark_value(self, value):  
        if self.won:
            return -1
        if value in self.locations:
            r,c = self.locations[value]
            self.board[r][c] = 1
            
            if np.sum(self.board[:,c]) == 5 or np.sum(self.board[r,:]) == 5:
                return self.calc_score(value)

        return -1
    
    def calc_score(self, value):
        summer = 0
        for prev_value in self.locations:
            r,c = self.locations[prev_value]
            if self.board[r][c] == 0:
                summer += int(prev_value)
        
        return summer * int(value)

def solver():
    values = [i.strip() for i in open("input.txt", "r")]
    
    input_sequence = values[0]
    input_sequence = input_sequence.split(",")
    
       
    boards = []
    start_ptr = 2
    end_ptr = 7
    while end_ptr <= len(values):
        tmp = values[start_ptr:end_ptr]
        new_board = board(tmp)

        boards.append(new_board)
        start_ptr+=6
        end_ptr+=6
        
    for i in input_sequence:    
        for bingos in boards:
            tmp = bingos.mark_value(i)
            if tmp != -1:
                return tmp
            
def solver_2():  
    
    values = [i.strip() for i in open("input.txt", "r")]
    
    input_sequence = values[0]
    input_sequence = input_sequence.split(",")
    start_ptr = 2
    end_ptr = 7
    
    boards = []
    
    while end_ptr <= len(values):
        tmp = values[start_ptr:end_ptr]
        new_board = board(tmp)

        boards.append(new_board)
        start_ptr+=6
        end_ptr+=6
    
    left = len(boards)
    
    for i in input_sequence:    
        for bingos in boards:
            tmp = bingos.mark_value(i)
            if tmp != -1:
                left -= 1
                if left == 0:
                    return tmp
            
    
print(solver())
print(solver_2())    