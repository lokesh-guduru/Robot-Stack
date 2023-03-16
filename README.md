# Robot Stack
This project was completed for a problem provided in Algorithms course at part of coursework at USF. The problem involves calculating the number of combinations of stacks that can be created using robots of certain height.

## Usage
The code requires an input file to run, which is provided as a command line argument. To run the code, use the following command:

python filename.py inputfile.txt

The input file should have the following format:

r1,s1,h1
r2,s2,h2
...

Where r is the number of robots, s is the number of stacks and h is the height of each robot. Each line of the file represents a different input case

## Code
The code reads the input file, splits and strips the lines to obtain the values for the number of robots, number of stacks and height of each robot. The 'combinations' function then calculates the total number of combinations of stacks that can be created using robots of certain height. The output is printed for each input case.

The code uses the 'numpy' module for reshaping the input values, and the 'sys' module for opening the input file. The code also uses a global variable 'total_combinations' for memoization purposes.

Refer report for more information.
