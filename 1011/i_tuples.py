#tuples are immutable.

numbers = (1, 2, 3)
print(numbers[0])

#error
numbers = (1, 2, 3)
numbers[0] = 10
print(numbers[0])