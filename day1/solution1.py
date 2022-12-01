import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines_int_safe(file_input)
pr(i_s, input)

dct = {}        
cnt = 1
for i in input:
    if i != -1:
        if cnt not in dct:
            dct[cnt] = 0
        dct[cnt] +=i
    else:
        cnt+=1
print(max(dct.values()))        

        
