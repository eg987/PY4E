fhand = open('mbox-short.txt')
dictionary = {}
count = 0
for line in fhand:
    if not line.startswith('From '):
        continue
    else:
        #line = line.rstrip()
        words = line.split()
            
        if words[2] not in dictionary:
            dictionary[words[2]] =  1
        else:
             dictionary[words[2]] += 1
print(dictionary)
        
