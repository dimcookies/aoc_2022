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
input=[[i[0], int(i[1])]for i in input]
pr(i_s, input)    

h_coords = [0,0]
t_coords = [0,0]
res = set()
res.add(str(t_coords))

def move_tail(move):
    if abs(h_coords[0] - t_coords[0]) <2 and abs(h_coords[1] - t_coords[1]) <2:
        return
    if h_coords[0] == t_coords[0]:
        if move == 'U':
            t_coords[1]+=1
        else:
            t_coords[1]-=1
    elif h_coords[1] == t_coords[1]:
        if move == 'L':
            t_coords[0]-=1
        else:
            t_coords[0]+=1
    else:
        if move == 'L':
            t_coords[0]-=1
            t_coords[1]=h_coords[1]
        elif move == 'R':
            t_coords[0]+=1
            t_coords[1]=h_coords[1]            
        elif move == 'U':
            t_coords[1]+=1
            t_coords[0]=h_coords[0]            
        else:
            t_coords[1]-=1
            t_coords[0]=h_coords[0]            


for i in input:
    pr(i_s, i)
    for j in range(1,i[1]+1):
        if i[0] == 'U':
            h_coords[1]+=1
        elif i[0] == 'D':
            h_coords[1]-=1
        elif i[0] == 'L':
            h_coords[0]-=1
        else:
            h_coords[0]+=1
        move_tail(i[0])
        res.add(str(t_coords))
        pr(i_s,h_coords)
        pr(i_s,t_coords)

print(len(res))    