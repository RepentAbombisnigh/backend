# (x, y)
# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 1)
# (1, 2)

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')
        
numbers = [5, 2, 5, 2, 2]
for item in numbers:
    print('x' * item)
    

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)