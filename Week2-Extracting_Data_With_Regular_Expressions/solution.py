# Week 2 - Assignment to find all numbers in a txt file and to sum them up

import re

# Open the text file, either regex_sum_42.txt or regex_sum_869366.txt
file = open("./regex_sum_42.txt")
sum_ = 0

for line in file:
    # Look for numbers, one or more
    num_lst = re.findall('[0-9]+',line)
    
    # If no number found in the line, go to the next line
    if len(num_lst) == 0: continue
    
    # Sum all the numbers found in the line
    sum_ += sum([int(d) for d in num_lst])
    
print("Sum: ",sum_)
