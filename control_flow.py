# Control Flow

# 1) If/ Else Statements
# 2) For loops
# 3) While loops

a = True
b = True
c = False
if a:
    print('It is true')
    print('Print this also')
    if b:
        print('It is true')
        if c:
            print('It is false')
else:
    print('It is false')
print('Always print this')

# 2) FOR LOOPS

a = [1, 2, 3, 4, 5]

#for that item in the list do something
for item in a:
    print(item)


# 3) WHILE LOOPS

a = 0
while a < 5:
    print(a)
    a = a + 1


