# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 07:25:06 2021

@author: hongb
"""


import numpy as np
from functools import reduce


def print_card(card):
    for line in card:
        print(line)


def merge_lists(list_of_lists):
    return reduce(lambda x, y: x + y, list_of_lists)


def make_some_cards(data):
    data = [int(x) for x in data if x]
    return [data[x : x + 25] for x in range(0, len(data), 25)]


def dobber(call, card):
    return [-1 if x == int(call) else x for x in card]


def check_row(card):
    for r in [card[x : x + 5] for x in range(0, len(card), 5)]:

        if sum(r) == -5:
            return card
        else:
            return False


def count_points(winning_card, last_call):
    #flat_list = merge_lists(winning_card)
    no_dobbed = [x for x in winning_card if x > -1]
    return sum(no_dobbed) * last_call


def check_col(card):
    one = [] 
    two = []
    three = []
    four = []
    five = []

    for c in range(0, 25, 5):  
        one.append(card[c + 0])
        two.append(card[c + 1])
        three.append(card[c + 2])
        four.append(card[c + 3])
        five.append(card[c + 4])

        if(sum(one) == - 5 or sum(two)  == - 5  or sum(three) == - 5  or sum(four) == - 5 or sum(five)  == - 5 ):
            return card

    return False

def final_bits(vals, call):
    if vals:
        print(vals)
        # print(vals)
        print("This winner is...")
        print_card([vals[x : x + 5] for x in range(0, len(vals), 5)])
        print("With a score of...")
        winner = count_points(vals, int(call))
        print(winner)
        return winner


    #return False

def test_main():
    data = open("input.txt").read().strip("\n\n").split()
    calls = data[0].split()[0].split(",")
    data.pop(0)
    card_data = make_some_cards(data)

    winner = -1

    # go through all the calls
    for index, call in enumerate(calls):
        for idx, card in enumerate(card_data):

            if winner == -1:

                dobbed_card = card_data[idx] = dobber(call, card)
                rows = check_row(dobbed_card)
                col = check_col(dobbed_card)

                col_check = final_bits(col, call)
                row_check = final_bits(rows, call)
                
                if row_check:
                    winner = row_check
                    print(idx, index)
                    break

                if col_check:
                    winner = col_check 
                    print(idx, index)
                    break

test_main()