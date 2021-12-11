# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 12:55:59 2021

@author: hongb
"""
def score(opener):
    score_string = opener[::-1]
    score = 0
    
    for char in score_string:
        score *= 5
        if char == "(":
            score += 1
        elif char =="[":
            score += 2
        elif char == "{":
            score += 3
        elif char == "<":
            score +=4
    return score
    
    

values = [i.strip() for i in open("input.txt", "r")]

points = 0

opens = "([{<"

closes = ")]}>"

incompletes = []


for line in values:
    corrupt = False
    openers = ""
    for char in line:        
        if char in opens:
            openers += char
        else:
            mirror = opens[closes.find(char)]
            if mirror != openers[-1]:

                if char == ")":
                    points += 3
                elif char == "]":
                    points += 57
                elif char =="}":
                    points += 1197
                else:
                    points += 25137
                corrupt = True
                break
            else:
                openers = openers[:-1]
    if not corrupt:
        incompletes.append(openers)
  
                
print(points)
#411471

points2 = []

for openers in incompletes:
    points2.append(score(openers))

points2.sort()

print(points2[len(points2)//2])
#3122628974