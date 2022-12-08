from re import S
import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
import os
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

def find_count(val, ar):    
    cnt = 0
    for i in ar:
        cnt+=1
        if i >= val:            
            break    
    #print(val,ar,cnt)        
    return cnt 

input = my_input.readlines_int_array_single(file_input)
pr(i_s, input)    
print(len(input),len(input[0]))
cnt = 0
res = []
for i in range(1,len(input)-1):
    for j in range(1,len(input[0])-1):        
        num = input[i][j]
        row=input[i]
        cnt1=find_count(num, row[:j][::-1])
        cnt2=find_count(num, row[j+1:])
        col = [row[j]for row in input]
        
        cnt3=find_count(num, col[:i][::-1])
        cnt4=find_count(num, col[i+1:])
        res.append(cnt1*cnt2*cnt3*cnt4)
        #print()
        

print(sorted(res,reverse=True)[0])