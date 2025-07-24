fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
max_count = 0
max_address = " "
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
for words in dictionary:
    if dictionary[words] > max_count:
        max_count = dictionary[words]
        max_address = words
        
print(max_address, max_count)
    #i need to work on last section line 19 down, as I had to look that up. 
    
    