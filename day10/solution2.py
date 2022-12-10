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
cycle = -1
idx=0
pending = None
res = 0
pixel=0

while True:
    cycle+=1
    if cycle == 240:
        break
    pixel= cycle%40

    if(pixel==0):
        print("\n",end="")

    if pixel in range(reg_X-1,reg_X+2):
        print("#",end="")
    else:
        print(".",end="")      

    if pending:
        idx+=1
        reg_X +=pending
        pending = None
    elif input[idx][0] == 'noop':
        idx+=1
    elif input[idx][0] == 'addx':
        pending = int(input[idx][1])

  
    
print()
        

