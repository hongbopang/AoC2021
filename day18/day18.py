# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 18:18:03 2021

@author: hongb
"""
import json
import copy
class snailfish:
    
    def __init__(self, values = (0,0), level = 0, parent = None):
        v1, v2 = values
        self.level = level
        self.numbers = 0
        self.snails = 0
        self.parent = parent        

        if type(v1) == int:
            self.left = int(v1)
            self.numbers += 1
        else:
            self.left = snailfish(v1, level = self.level+1, parent = self)
            self.snails +=1
            
        if type(v2) == int:
            self.right = int(v2)
            self.numbers += 1
        else:
            self.right = snailfish(v2,  level =self.level+1, parent = self)
            self.snails += 1

            
    def reveal_secrets(self):
        tmp = []
        if type(self.left) == int:
            tmp.append(self.left)
        else:
            tmp.append(self.left.reveal_secrets())
        
        if type(self.right) == int:
            tmp.append(self.right)
        else:
            tmp.append(self.right.reveal_secrets())
        return tmp
        
        
    def adder_right(self, val):
        if type(self.right) == int:
            self.right += val
        else:
            self.right.adder_right(val)
            
    def find_parent_with_left(self,val,source):
        if type(self.left) == int:
            self.left += val
            return
        if source == self.left:            
            if self.parent == None:
                return        
            else:
                self.parent.find_parent_with_left(val,self)                
        else:
            self.left.adder_right(val)
            
            
    def adder_left(self, val):
        if type(self.left) == int:
            self.left += val
        else:
            self.left.adder_left(val)
            
    def find_parent_with_right(self,val,source):
        
        if type(self.right) == int:
            self.right += val
            return
        if source == self.right:  
            if self.parent == None:
                return        
            else:
                self.parent.find_parent_with_right(val,self)                
        else:
            self.right.adder_left(val)

    def explode(self):        
        if type(self.left) != int:
            v1, v2 = self.left.left, self.left.right
            self.left = 0
            self.snails -= 1
            self.numbers += 1            
            if type(self.right) == int:
                self.right += v2
            else:                
                self.right.adder_left(v2)
            if self.parent:
                self.parent.find_parent_with_left(v1,self)
            
        elif type(self.right) != int:
            
            v1, v2 = self.right.left, self.right.right
            self.right = 0
            self.snails -= 1
            self.numbers += 1
            if type(self.left) == int:
                self.left += v1
            else:                
                self.left.adder_right(v1)
            if self.parent:
                self.parent.find_parent_with_right(v2,self)
            
    def check_to_explode(self):        
        if self.level >= 4 and self.numbers == 2:
            self.parent.explode()
            return 1
        
        else:            
            if type(self.left) != int:                
                tmp = self.left.check_to_explode()
                if tmp == 1:
                    return 1
                
            if type(self.right) != int:
                tmp = self.right.check_to_explode()
                if tmp == 1:
                    return 1
        return 0
        
    def check_to_split(self):
        if type(self.left) != int:
            tmp = self.left.check_to_split()
            if tmp == 1:
                return 1
            
        if type(self.left) == int and self.left >= 10:
            self.split(-1)
            return 1
        
        if type(self.right) != int:
            tmp = self.right.check_to_split()
            if tmp == 1:
                return 1
            
        if type(self.right) == int and self.right >= 10:
            self.split(1)
            return 1
        
        
        return 0
    
    def split(self, arg):
        self.numbers -= 1
        self.snails += 1
        if arg == -1:
            tmp = self.left
            v1 = tmp // 2
            v2 = tmp - v1
            
            new_snail = snailfish([v1,v2], level = self.level + 1, parent = self)
        
            self.left = new_snail
        else:  
            tmp = self.right
            v1 = tmp // 2
            v2 = tmp - v1
            
            new_snail = snailfish([v1,v2], level = self.level + 1, parent = self)
        
            self.right = new_snail
            
    def update_level(self):
        self.level += 1
        
        if type(self.left) != int:
            self.left.update_level()
        if type(self.right) != int:
            self.right.update_level()
            
    def reduce(self):       
        while 1:
            tmp = self.check_to_explode()
            if tmp == 1:
                continue
            tmp = self.check_to_split()
            if tmp == 1:
                continue
            return
        
        
    def magnitude(self):
        if type(self.left) == int:
            val1 = self.left
        else:
            val1 = self.left.magnitude()
        
        if type(self.right) == int:
            val2 = self.right
        else:
            val2 = self.right.magnitude()  
        return 3*val1 + 2*val2
            
def add(first,second):
    first = copy.deepcopy(first)
    second = copy.deepcopy(second)
    new_parent = snailfish()
    new_parent.left = first
    new_parent.right = second
    first.parent = new_parent
    second.parent = new_parent
    new_parent.left.update_level()
    new_parent.right.update_level()
        
    return new_parent
               

lines = [i.strip() for i in open("input.txt", "r")]

snails = []

for l in lines:
    res = json.loads(l)
    tmp = snailfish(res)
    snails.append(tmp)
master_snail = snails[0]
snails2 = [i for i in snails]
for i in range(1,len(snails)):
    new_snail = add(master_snail,snails[i])
    new_snail.reduce()
    master_snail = new_snail

print(master_snail.magnitude())
ans2 = 0

for i in range(len(snails2)):
    for j in range(len(snails2)):
        if i != j:
            tmp = add(snails2[i],snails2[j])
            tmp.reduce()

            ans2 = max(ans2,tmp.magnitude())
print(ans2)


