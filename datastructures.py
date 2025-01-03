# Data structures in python are 
# 1) Lists
# 2) Sets
# 3) Tuples
# 4) Dictionaries

# 1) Lists or arrays defined with []

my_list = ['apple', 'mango', 1, True]
#can add things to a list by using .append

my_list.append('pear')

# The update list should look like:

my_list = ['apple', 'mango', 1, True, 'pear']

#Check the lenght of the list by using len(nameoflist) function

len(my_list) #should output 5

# You can have a list inside a list:
my_list2 = [[1,2, 3], 'pear']

len(my_list2) #should be 2

# 2) Sets are defined with {} 
# Each element in the set should be unique
# The order matters {1, 2} does not equal {2, 1}
# E.g. if there's a duplicate the set will treat it as a one element

my_set = {1, 2, 2, 3}
print(my_set)
len(my_set) #output should be 3

# 3) Tuples are defined with ()
# order in a tuple matters as well
# You cannot modify tuples it has to remain the same
# so append will not work
# use it when you knwo you wont modify your list better for memory
# computer will not take as much space in the memory
# good to store coordinates like x, y. It is way more efficient than a list

my_tuple = (1, 2, 3)


# 4) Dictionaries
# Use them a lot very different from the above data structures
# you have a key and a value assigned to it 
# like a dictionary in the real life when you look up a word and then you get a definiton the
# the purpose is the same
# defined with curly brackets
# the order does not matter
# if you name two keys the same name the second one with overwrite the first one


my_dictionary = {
    'apple': 'My favorite fruit',
    'pear': "My sister's favorite fruit"
}

my_dictionary('apple') # will show 'My favorite fruit'