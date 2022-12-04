import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines(file_input)
pr(i_s, input)    

cnt=0
for i in input:
    ar=i.split(",")
    r1 = [int(j) for j in ar[0].split("-")]
    r2 = [int(j) for j in ar[1].split("-")]
    if (r1[0]<=r2[0] and r1[1]>=r2[1]) or (r2[0]<=r1[0] and r2[1]>=r1[1]) or (r1[1]>=r2[0] and r1[0] <=r2[0]) or (r2[1]>=r1[0] and r2[0] <=r1[0]):
        cnt +=1
        pr(i_s, ar)    
        
print(cnt)        