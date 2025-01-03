# We can apply the same properties
# without the need to repeat it every time

# start with def then name of the function and what it takes
def multiplybythree(val):
    3 * val

multiplybythree(4) # This will ouput 12

def multiply(val1, val2):
    val1 * val2

multiply(2, 5) # should return 10

a = [1, 2, 3]

def appendFour(myList):
    myList.append(4)

appendFour(a)
print(a)

