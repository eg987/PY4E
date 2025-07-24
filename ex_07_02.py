fname = input('Enter the file name: ')
count = 1
total = 0
try: 
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    quit()
for line in fhand:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    else: 
        my_num = line[20:]
        #print (count, my_num)
        count = count +1
        total = float(total) + float(my_num)
#print("avg:", total, "/", (count-1), "=", (total/count))
#total = float(total)
count = (float(count)-1)
#print(total, count)
avg = float(total/count)
print("Average spam confidence:", avg)

    
    #very clunky should edit when skills are better