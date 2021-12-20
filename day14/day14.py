# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 12:50:38 2021

@author: hongb
"""
import copy

def get_ans(parents_counter):
    letters=dict()
    for key in parents_counter:
        char1 = key[0]
        char2 = key[1]
        
        if char1 not in letters:
            letters[char1] = 0
        if char2 not in letters:
            letters[char2] = 0
            
        letters[char1] += parents_counter[key] 
        letters[char2] += parents_counter[key] 
    
    letters[template[0]] += 1    
    letters[template[-1]] += 1   
    nums = []
    for key in letters:
        nums.append(letters[key]//2)
    print(max(nums)-min(nums)) 

lines = [i.strip() for i in open("input.txt", "r")]

template = lines[0]

parents = dict()

for i in range(2,len(lines)):
    tmp = lines[i].split(" -> ")
    original, inserter = tmp
    a1,a2 = original[0],original[1]    
    parent = original
    children = [a1+inserter, inserter+a2]
    parents[parent] = children

parents_counter = dict()

for i in range(len(template)-1):
    tmp = template[i:i+2]
    if tmp not in parents_counter:
        parents_counter[tmp] = 0
    parents_counter[tmp] += 1
    
for _ in range(40):
    tmp_counter = dict()
    
    for key in parents_counter:
        c1,c2 = parents[key]
        if c1 not in  tmp_counter:
            tmp_counter[c1] = 0
        if c2 not in tmp_counter:
            tmp_counter[c2] = 0
            
        tmp_counter[c1] += parents_counter[key]
        tmp_counter[c2] += parents_counter[key]
    parents_counter = copy.deepcopy(tmp_counter)
    if _ == 9:
        get_ans(parents_counter)

get_ans(parents_counter)



