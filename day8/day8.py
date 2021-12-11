# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 12:44:24 2021

@author: hongb
"""
def decode(words_in, output):
    twos = []
    fours = []
    counter_track = dict()
    
    for word in words_in:
        
        if len(word) == 2:
            twos = [char for char in word]
        elif len(word) == 4:
            fours = [char for char in word]
        for char in word:
    
            if char not in counter_track:
                counter_track[char] = 0
            counter_track[char] += 1
    
    top, left_up, right_up, mid, left_bot, right_bot,bots = 0,0,0,0,0,0,0
    
    for letter in counter_track:
        val = counter_track[letter]
        if val == 6:
            left_up = letter
        elif val == 4:
            left_bot = letter
        elif val == 9:
            right_bot = letter
        elif val == 7:
            if letter in fours:
                mid = letter
            else:
                bot = letter
        elif val == 8:
            if letter in twos:
                right_up = letter
            else:
                top = letter
    ans = 0
    for word in output:
        ans *= 10
        if len(word) == 2:
            ans += 1
        elif len(word) == 4:
            ans += 4
        elif len(word) == 3:
            ans += 7
        elif len(word) == 7:
            ans += 8
    
        elif len(word) == 6:
            if mid not in word:
                ans += 0
            elif right_up not in word:
                ans += 6
            elif left_bot not in word:
                ans += 9
        elif len(word) == 5:
            if right_up not in word:
                ans += 5
            elif right_bot not in word:
                ans += 2
            else:
                ans += 3
    return ans


values = [i.strip().split(" | ") for i in open("input.txt", "r")]

lengths = dict()
lengths[0] = 6
lengths[1] = 2
lengths[2] = 5
lengths[3] = 5
lengths[4] = 4
lengths[5] = 5
lengths[6] = 6
lengths[7] = 3
lengths[8] = 7
lengths[9] = 6

counter = 0

ans2 = 0

for line in values:
    ins, outs = line
    ins = ins.split()
    outs = outs.split()
   
    words = outs
    for word in words:
        if len(word) in [2,4,3,7]:
            counter += 1
            
    tmp = decode(ins, outs)
    ans2 += tmp
            
print(counter)
#284
print(ans2)
#937499




   




