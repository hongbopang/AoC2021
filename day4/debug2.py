# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 19:55:12 2021

@author: hongb
"""


with open('input.txt', 'r') as input_data:
    for line in input_data:
        row_ls_raw = line.strip().split(" ")
        print(row_ls_raw)