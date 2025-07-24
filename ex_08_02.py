#exercise = 'Exercise 8.2.1'

# Origial file
# fhand = open('mbox-short.txt')

# Edit the file program-fail.txt so that the rest of the code fails!
fhand = open('program-fail.txt')

count = 0
for line in fhand:
    words = line.split()
    print('Debug:', words)
    if len(words) == 0 or len(words) < 3:
        continue
    if words[0] != 'From':
        continue
    print(words[2])