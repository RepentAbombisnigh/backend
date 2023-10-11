numbers = [5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)

#if you want to put in the middle (the first to where, which number)
numbers = [5, 2, 1, 7, 4]
numbers.insert(0, 10)
print(numbers)

#to delete certain data
numbers = [5, 2, 1, 7, 4]
numbers.remove(5)
print(numbers)

#delete all
numbers = [5, 2, 1, 7, 4]
numbers.clear()
print(numbers)

#delete the last data
numbers = [5, 2, 1, 7, 4]
numbers.pop()
print(numbers)

#to find the data's position.
#if there is none, it will err
numbers = [5, 2, 1, 7, 4]
print(numbers.index(5))

#to confirm the existance of data
numbers = [5, 2, 1, 7, 4]
print(50 in numbers)

#counting the data
numbers = [5, 2, 1, 5, 7, 4]
print(numbers.count(5))

#to sort
numbers = [5, 2, 1, 7, 4]
numbers.sort()
# numbers.reverse()
print(numbers)

numbers = [5, 2, 1, 7, 4]
numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)