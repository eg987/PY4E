handle = open('words.txt')
dw = dict()
count = 0
for line in handle:
    words = line.split()
    print(words)
    for x in words:
        count += 1
        if x in dw :
            continue
        else:
            dw[x] = count
handle.close()            
print(dw) 

#index of unique words