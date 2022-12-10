from re import S
import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
import os
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines_array(file_input)
pr(i_s, input)    

reg_X = 1
cycle = 0
idx=0
pending = None
res = 0

while True:
    cycle+=1
    if cycle == 221:
        break

    if cycle in (20, 60,100,140,180,220):
        print(cycle, reg_X)    
        res +=cycle*reg_X

    pr(i_s,str(idx)+ " " + str(input[idx]))
    if pending:
        idx+=1
        reg_X +=pending
        pending = None
    elif input[idx][0] == 'noop':
        idx+=1
    elif input[idx][0] == 'addx':
        pending = int(input[idx][1])
    pr(i_s,"\t" + str(cycle) + " " + str(reg_X))
    
print(res)        
        

