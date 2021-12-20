# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 12:52:30 2021

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
    go = True
    
    while 1:
        temp_s = string[s:e]
        checker = temp_s[0]
        temp_s = temp_s[1:]
        ansString += temp_s
        
        if checker == '0':
            return ansString, e
        
        s += 5
        e += 5
   

def parse_packet(string, ptr):            
    version = string_to_dec(string[ptr:ptr+3])
    ID = string_to_dec(string[ptr+3:ptr+6])
    print("\n")
    print(string[ptr:])
    print(version, ID, ptr)
    if ID == 4:
        print('literal')
        ansString, ptr = parse_literal(string, ptr+6)
        
    else:
        ptr += 6
        length = string[ptr]
        ptr += 1
        if length == '0':
            print('0 mode')
            len_of_sub = string_to_dec(string[ptr:ptr+15])
            print("length is ", len_of_sub)
            ptr += 15
            target_ptr = ptr + len_of_sub
            while ptr < target_ptr:
                print(ptr,target_ptr)
                ptr, v_n = parse_packet(string, ptr)
                version += v_n

        else:
            print('1 mode')
            n_of_packet = string_to_dec(string[ptr:ptr+11])
            counter = 0
            print("n_packets =", n_of_packet )
            ptr = ptr+11
            while counter != n_of_packet:
                ptr, v_n = parse_packet(string, ptr)
                version += v_n
                counter += 1
    
    return ptr, version
    

lines = [i.strip() for i in open("input.txt", "r")][0]

bits = ""

for char in lines:
    bits += translator[char]

ptr = 0
total = 0
print(bits[40:63])
while ptr < len(bits)-7:

    ptr, v_n = parse_packet(bits, ptr)

    total += v_n
    print(total)


