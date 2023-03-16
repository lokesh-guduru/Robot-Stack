#Importing required modules
import sys
import numpy as np
#Opening input file
input_file = open(sys.argv[1], "r")
i = []
#Reading input file
for line in input_file.readlines():
   #Splitting and stripping the input lines 
   i += line.strip('\n').split(',')
#Closing the file
input_file.close()
#i = np.reshape(i,3*len(i))
i = [int(x) for x in i]

#Defining combinations function
def combinations(robots, stacks, height):
    global total_combinations
    #Defining base cases
    if robots == 0:
        return 1
    if stacks == 0 or robots < 0:
        return 0
    #If doesn't meet the sentinal value, returning memoization value
    if total_combinations[stacks][robots]:
            return total_combinations[stacks][robots]
    #Recurrecne call
    total_combinations[stacks][robots] = combinations(robots-1, stacks, height) + combinations(robots, stacks-1, height) - combinations(robots-height-1, stacks-1, height)
    return total_combinations[stacks][robots]

#Taking temp variable for output
ind_inp = 0
while ind_inp < len(i):
    #Initialization
    total_combinations = [[0 for x in range(i[ind_inp]+1)] for y in range(i[ind_inp+1]+1)]
    #Printing output
    print(tuple(i[ind_inp: ind_inp+3]),'=', combinations(i[ind_inp],i[ind_inp+1],i[ind_inp+2]))
    ind_inp = ind_inp + 3
  