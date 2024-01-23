

dis = {
    'name': 'anand sharma',
    'age': 26,
    'gender': 'male'
}

print(dis['name'])

dis['work'] = 'software Engineer'
print(dis)

dis['work'] = 'software engineer'

print(dis)

del dis['gender']

print(dis)

dis.clear()
print(dis)

odd_square = {num :num**2 for num in range(1,6) if num % 2 !=0}
print(odd_square)



dic1 = {
    'a':1,
    'b': 2,
}
dic2 = {
    'a':10,
    'c': 2,
}

new_dic = {**dic1, **dic2}

print(new_dic)