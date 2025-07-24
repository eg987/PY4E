
#word = 'banana'
word = input("Enter a word: ")
def count(word, desired):
    count = 0
    for letter in word:
        if letter == desired:
            count = count + 1
    print(count)
    
count(word, "a")
#how can count be used as variable and function name?