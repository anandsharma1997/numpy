

fruits = ['apple', 'banana', 'graps', 'cheeku']

print(fruits[0])

print(fruits[2:4])

fruits.append('papaya')

print(fruits)

names = ['anand', 'vinay', 'shalini']

fruits.extend(names)
print(fruits)

fruits.insert(1, 'instered')
print(fruits)
fruits.remove('vinay')
print(fruits)

fruits.pop(3)
print(fruits)


square = [x**2 for x in range(100)]
print(square)