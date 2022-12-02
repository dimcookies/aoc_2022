import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines_str_array(file_input)
pr(i_s, input)    

def win(they, we):
    if (they == 'A' and we == 'X') or (they == 'B' and we == 'Y') or (they == 'C' and we == 'Z'):
        return 3
    if (they == 'A' and we == 'Z') or (they == 'C' and we == 'Y') or (they == 'B' and we == 'X'):
        return 0
    return 6


score =0        
for i in input:
    if i[2] == 'X':
        score+=1
    elif i[2] =='Y':
        score+=2
    else:
        score+=3
    score+=win(i[0],i[2])

print(score)
    