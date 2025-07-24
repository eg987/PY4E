my_list = []
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    text = line.rstrip()
    words = text.split()
    for word in words:
        if word in my_list:
            continue
        else:
            my_list.append(word)
print(sorted(my_list))
    