#My 2nd list!

#Make an empty list as such:
#my_list = []

#Now make a program that does the following:

#1. Add the integers 2, 1 and 3 to the list

#2. Add the string “cyber” to the list

#3. Print the index of “cyber”

#4. Remove the string from the list

#5. Put the list in ascending order and print it

# Create an empty list
my_list = []

# 1. Add integers 2, 1, and 3
my_list.append(2)
my_list.append(1)
my_list.append(3)

# 2. Add the string "cyber"
my_list.append("cyber")

# 3. Print the index of "cyber"
print(my_list.index("cyber"))

# 4. Remove the string from the list
my_list.remove("cyber")

# 5. Sort the list in ascending order and print it
my_list.sort()
print(my_list)

# 6.
my_list.reverse()
print(my_list)