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