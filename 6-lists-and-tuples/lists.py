users = ['Ismail', 'Abdullah', 'Noor']

data = ['Ismail', 42, True]

emptylist = []

#
# to check if a value exists in a list
#
print("Ismail" in users)
print("Ismail" in data)
print("Ismail" in emptylist)

#
# specific values in a list
#
print(users[0])  # 1st in list
print(users[-1])  # last in list
print(users[-2])  # 2nd last in list

#
# give index of that value
#
print(users.index("Noor"))

#
# give values in a specific range of indexes
#

# give value of 0-2 position will not include the value at index 2
print(users[0:2])
# start from a specific index and the give all values
print(users[1:])
# for negative indexes
print(users[-3:-1])

#
# length of list
#
print(len(data))

# add more items to an already created list
users.append("Mirza")
print(users)

#
# add another list into a pre-existing list
#

# 1 iteration
users += ['Taher']
print(users)

# make sure you add a list here in iteraion
# if you were to add string instead of a list, it would add every letter as an individual value in the list e.g. 'i', 's', 'm', 'a', 'i', 'l'

# users += 'Taher'
# print(users)

# 2 extend method
users.extend(['Muhammad', 'Valorant'])
print(users)

# add another list into a list using variable
users.extend(data)
print(users)

#
# insert into a specific index
#

# insert method
users.insert(0, 'Bob')
print(users)

# insert using range to replace
# x:x start & end at the same position
users[2:2] = ["Eddie", "Alex"]
print(users)

#
# replace method
# will replace items in starting from x ending at y-1 in x:y
users[1:3] = ['Robert', 'JPJ']
print(users)


#
# remove method
# remove a specific item from a list
users.remove("Bob")
print(users)

#
# pop method
# will rmeove the last item from the list & also return that value
print(users.pop())
print(users)

#
# del keyword
#

del users[0]  # delete first item
print(users)

# delete the whole list
# del data
# print(data)


#
# clear method
# empty or clear out the whole list, the list will still exist but with no items in it
data.clear()
print(data)


users.pop()

#
# sort method
#
users[1:2] = ['dave']
# will sort all items alphabetically, also first it sorts all the uppercase, then the lowercase words
users.sort()
print(users)

# to include lowercase words in the sorting along with the uppercase/propercase ones
# now dave will be sorted alphabetically along with all other items
users.sort(key=str.lower)
print(users)

# NOTE: it will not sort between different data types, will throw error in that case
