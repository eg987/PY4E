'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
#Sample line: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Sample Execution:
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
'''


fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fhand = open(fname)
dictionary = {}
count = 0
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From '):
        continue
    else:
        words = line.split()
        time = (words[5])
        hourlist = time.split(":")
        hour = hourlist[0]
        if hour not in dictionary:
            dictionary[hourlist[0]] =  1
        else:
             dictionary[hourlist[0]] += 1
final= sorted(dictionary.items())
for k, v in final:
    print(k, v)

#times_list=list()
#for (k,v) in dictionary.items():
#    times_list.append((v,k))
#times_list = sorted(times_list)
#print(times_list)
