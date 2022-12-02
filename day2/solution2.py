import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines_str_array(file_input)
pr(i_s, input)    

def win(they, result):
    if result == 'X':
        if they =='A':
            return 3
        if they=='B':
            return 1
        return 2
    if result == 'Y':
        if they =='A':
            return 1
        if they=='B':
            return 2
        return 3
    if they =='A':
        return 2
    if they=='B':
        return 3
    return 1
    


score =0        
for i in input:
    if i[2] == 'X':
        score+=0
    elif i[2] =='Y':
        score+=3
    else:
        score+=6
    score+=win(i[0],i[2])

print(score)
    