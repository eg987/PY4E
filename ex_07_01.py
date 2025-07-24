#exercise = 'Exercise 7.1'

fname = input('Enter the file name: ')
try: 
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    quit()
#fhand = open('mbox-short.txt')
#print(fhand)
for line in fhand :
    line = line.rstrip()
    print(line.upper())
