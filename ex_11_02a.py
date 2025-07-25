'''
Exercise  11.2: Write a program to look for lines of the form

'New Revision: 39771'

and extract the number from each of the lines using a regular expression and
the findall() method. Compute the average of the numbers and print out the
average.

Enter file:mbox.txt
38549.7949721

Enter file:mbox-short.txt
39756.9259259

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
'''
import re
total=0
count=0
handle = open('regex_sum_42.txt')
for line in handle:
    line = line.rstrip()
    num = re.findall('([0-9]+)', line)
    ##need to be able to add multiple "numbers' per list
    # if len(number) != 1 : 
    #     continue
    for val in num:
        val = float(val) #convert string to float#
        total = total + val
        count += 1
avg = total / count
print("Total:", total)
    
# tot = sum(num)
# print("sum:", tot)
# things = len(num)
# print("items:", things)
# avg = tot/things
# print(avg)
