# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 12:02:01 2021

@author: hongb
"""
    
def fish_counter(original, steps):
    fish_count = [i for i in original]    
    
    for i in range(steps):
        new_count = [0 for _ in range(9)]
        
        for i in range(1, 9):
            new_count[i-1] += fish_count[i]
        new_count[6] += fish_count[0]
        new_count[8] += fish_count[0]
        fish_count = [i for i in new_count]
    return sum(fish_count)
    

values = [i.strip().split(",") for i in open("input.txt", "r")]

fishes = values[0]
fishcount = [0 for _ in range(9)]

for f in fishes:
    fishcount[int(f)] += 1

print(fish_counter(fishcount, 80))
print(fish_counter(fishcount, 256))


values = [i.strip().split(",") for i in open("input.txt", "r")]
fishes = values[0]
slow_fish = [int(f) for f in fishes]


for _ in range(80):
    new_fish = []
    for fish in slow_fish:
        if fish == 0:
            new_fish.append(8)
            new_fish.append(6)
            
        else:
            new_fish.append(fish - 1)
    slow_fish = [i for i in new_fish]
            
print(len(slow_fish))
    