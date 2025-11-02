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
users[2:2] = ["Eddie", "Alex"]
print(users)

#
# replace method
#
