# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 14:05:58 2021

@author: hongb
"""

translator = dict()
translator['0'] = '0000'
translator['1'] = '0001'
translator['2'] = '0010'
translator['3'] = '0011'
translator['4'] = '0100'
translator['5'] = '0101'
translator['6'] = '0110'
translator['7'] = '0111'
translator['8'] = '1000'
translator['9'] = '1001'
translator['A'] = '1010'
translator['B'] = '1011'
translator['C'] = '1100'
translator['D'] = '1101'
translator['E'] = '1110'
translator['F'] = '1111'

def string_to_dec(s):
    ans = 0    
    for char in s:
        ans *= 2
        ans += int(char)
    return ans    

def parse_literal(string, start):    
    ansString = ""    
    s,e = start,start+5
    
    while 1:
        temp_s = string[s:e]
        checker = temp_s[0]
        temp_s = temp_s[1:]
        ansString += temp_s
        
        if checker == '0':
            return string_to_dec(ansString), e
        
        s += 5
        e += 5
   

def parse_packet(string, ptr):            
    version = string_to_dec(string[ptr:ptr+3])
    ID = string_to_dec(string[ptr+3:ptr+6])

    if ID == 4:
        value, ptr = parse_literal(string, ptr+6)
        return value, ptr, version
    else:
        holder = []        
        ptr += 6
        length = string[ptr]
        ptr += 1
        
        if length == '0':
            len_of_sub = string_to_dec(string[ptr:ptr+15])
            ptr += 15
            target_ptr = ptr + len_of_sub
            while ptr < target_ptr:
                value, ptr, v_n = parse_packet(string, ptr)
                version += v_n
                holder.append(value)

        else:
            n_of_packet = string_to_dec(string[ptr:ptr+11])
            counter = 0
            ptr = ptr+11
            while counter != n_of_packet:
                value, ptr, v_n = parse_packet(string, ptr)
                version += v_n
                counter += 1
                holder.append(value)
        ans = 0  
        if ID == 0:
            ans = sum(holder)
        elif ID == 1:
            ans = 1
            for i in holder:
                ans *= i
        elif ID == 2:
            ans = min(holder)
        elif ID == 3:
            ans = max(holder)
        elif ID == 5:
            if holder[0] > holder[1]:
                ans = 1
        elif ID == 6:
            if holder[0] < holder[1]:
                ans = 1
        elif ID == 7:
            if holder[0] == holder[1]:
                ans = 1
        
        return ans, ptr, version
    

lines = [i.strip() for i in open("input.txt", "r")][0]

bits = ""

for char in lines:
    bits += translator[char]

ptr = 0
total = 0

while ptr < len(bits)-7:
    ans,ptr, v_n = parse_packet(bits, ptr)
    total += v_n
    
print(total,ans)


