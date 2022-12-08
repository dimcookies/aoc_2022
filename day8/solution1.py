from re import S
import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
import os
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines_int_array_single(file_input)
pr(i_s, input)    
print(len(input),len(input[0]))
cnt = 0
for i in range(1,len(input)-1):
    for j in range(1,len(input[0])-1):        
        num = input[i][j]
        row=input[i]
        #print(i,j,)
        if num > max(row[:j]):
            cnt+=1
            continue
        if num > max(row[j+1:]):
            cnt+=1
            continue
        col = [row[j]for row in input]
        
        if num > max(col[:i]):
            cnt+=1
            continue
        if num > max(col[i+1:]):
            cnt+=1
            continue

print(cnt + ((len(input)-1)*4))