exercise = 'Exercise 8.6'

### Start Code Here ###
#prompt person for input, when done calculate
nums = []
while True:
    n = input("Enter a number: ")
    if n == 'done' : break
    nums.append(n)
    
print("Maxium: ", max(nums))
print("Minimum: ", min(nums))
###  End Code Here  ###