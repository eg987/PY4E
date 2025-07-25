'''
Exercise 2: Write a program to look for lines of the form

`New Revision: 39772`
and extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average.

Example output:
Enter file:mbox.txt
38549.7949721

Enter file:mbox-short.txt
39756.9259259

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
'''
import re

handle = open('regex_sum_1706074.txt')
numlist=list()
sumlist=list()
for line in handle:
    line = line.rstrip()
    number = re.findall('([0-9]+)', line)
    ##need to be able to add multiple "numbers' per list
    if len(number) > 0 : 
        numlist.append(number)
    
for fnum in numlist:
    if type(fnum) is list:
        for item in fnum:
            item = float(item)
            sumlist.append(item)
    else:
        fnum = float(fnum)
        sumlist.append(fnum)
print(sum(sumlist))    
