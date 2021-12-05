# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 12:44:09 2021

@author: hongb
"""

class board:
    def __init__(self):
        self.board = [[" " for _ in range(5)] for __ in range(5)]
        self.marked = [[0 for _ in range(5)] for __ in range(5)]
        self.presents = dict()
        self.won = False
        
    def add_values(self, values):
        for i in range(5):
            splits = values[i].split()
            self.board[i] = [j for j in splits]
            for j in splits:
            
                self.presents[j] = 1
            
    def mark_value(self, value):
        if self.won:
            return -1
        if value in self.presents:
            for r in range(5):
                for c in range(5):
                    if self.board[r][c] == value:
                        self.marked[r][c] = 1                        
                        r_sum, c_sum = 0,0
                        for idx in range(5):
                            r_sum += self.marked[r][idx]
                            c_sum += self.marked[idx][c]
                        if r_sum == 5 or c_sum == 5:
                            self.won=True
                            return self.calc_score(value)
        return -1
    
    def calc_score(self, value):
        summer = 0
        for r in range(5):
            for c in range(5):
                if self.marked[r][c] == 0:
                    summer += int(self.board[r][c])
        return summer * int(value)

def solver():
    values = [i.strip() for i in open("input.txt", "r")]
    
    input_sequence = values[0]
    input_sequence = input_sequence.split(",")
    start_ptr = 2
    end_ptr = 7
    
    boards = []
    
    while end_ptr <= len(values):
        tmp = values[start_ptr:end_ptr]
        new_board = board()
        new_board.add_values(tmp)
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
        new_board = board()
        new_board.add_values(tmp)
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