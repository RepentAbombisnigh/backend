users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptylist = []

print("Dave" in emptylist)

print(users[0])
print(users[-1])

print(users.index('Sara'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append('Elsa')
print(users)

users += ['Jason'] # when using += sutff you should include brackets, otherwise, every character wil be regiested. 
print(users)

users.extend(['Rober', 'Jimmy'])
print(users)

# users.extend(data)
# print(users)

users.insert(0,'Bob') #insert as the first from the list
print(users)

users[2:2] = ['Eddie', 'Alex'] #3rd 4th
print(users)

users[1:3] = ['Robert', 'JPJ'] #replacement
print(users)

users.remove('Bob')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users.sort() # Alphabetical order
print(users) 

users[1:2] = ['dave'] # Alphabetical adding but Capital order > lower capital order
users.sort()
print(users)

users.sort(key=str.lower) 
print(users)

nums = [4,42,78,1,5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(nums)
print(mynums)
print(mycopy)
print(nums)

print(nums)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)