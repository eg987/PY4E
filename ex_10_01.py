fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fhand = open(fname)
dictionary = {}
count = 0
for line in fhand:
    if not line.startswith('From '):
        continue
    else:
        #print(line)
        words = line.split()
        if words[1] not in dictionary:
            dictionary[words[1]] =  1
        else:
             dictionary[words[1]] += 1

lst= list()
for k,v in dictionary.items():
    lst.append( (v,k))
lst=sorted(lst, reverse=True)
for count, email in lst[:1]:
    print (email, count)