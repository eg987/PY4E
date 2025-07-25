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