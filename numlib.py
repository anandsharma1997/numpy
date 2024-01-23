#Numpy creating Arrays

import numpy as np

# arr = np.array([1, 2, 3, 4, 5])

# print(arr, type(arr))

#We can use any type of data like list , tuple , set inside the array

#Dimensions in arrays

# 0-D

# arr = np.array(42)
# print(arr)

#1-D

# arr = np.array([1, 2, 3, 4])
# print(arr)

#2-D

# arr = np.array([[1,2,4,3],
#                 [5,6,7,8]])

# print(arr)


# Check number of dimensions

# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

#Numpy array indexing

# arr = np.array([1, 2, 3, 4, 5])
# print(arr[1] + arr[2])

#access 2d array

# arr = np.array([
#     [1,2,3],
#     [6,7,8]]
# )

# print("2nd element on the 1st row", arr[0,1])
# print("3rd element on 2nd row:", arr[1,2])


#Negative indexing

# arr = np.array([
#     [1,2,3,4,5],
#     [6,4,5,8,9]
# ])

# print("last element from 2nd dim:", arr[1,-1])


#numpy array slicing

# arr = np.array([1,2,3,4,5,6,7,8,9])
# print(arr[1:5])
# print(arr[4:])
# print(arr[0:4])
# print(arr[-4:-1])
# print(arr[1:6:2])
# print(arr[::2])



#Slicing 2-d array
# arr = np.array([
#     [1,2,3,4,5],
#     [6,7,8,9,10]
# ])

# print(arr[1, 1:4])
# print(arr[0:2, 2])



# Numpy Data types
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

# arr = np.array([1,2,3,4])
# print(arr.dtype)

# arr = np.array(['anand', 'vinay', 'kuldeep', 'rakhi'])
# print(arr.dtype)



# Creating arrays woth a defined data type

# arr = np.array([1,2,3,4,5,6], dtype='S')
# print(arr)
# print(arr.dtype)

# arr = np.array([1,2,3,4,5,6], dtype='i4')
# print(arr)
# print(arr.dtype)


# arr = np.array([1.1, 2.1, 3.5])
# newarr = arr.astype(int)
# print(newarr)
# print(newarr.dtype)


# The difference between copy and view

#The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
#The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.


#Copy

# arr = np.array([1,2,3,4,5])
# copy_arr = arr.copy()

# arr[0] = 42

# print(arr, copy_arr)


# #View

# view_arr = arr.view()
# arr[0] = 52

# view_arr[3] = 100

# print(arr, view_arr)

# #Check if array owns its data
# print(copy_arr.base, view_arr.base)



# Numpy Array shape

# arr = np.array([
#     [1,2,3,4,5],
#     [4,5,6,4,8]
# ])

# print(arr.shape)

# arr = np.array([1, 2, 3, 4], ndmin=5)

# print(arr)
# print('shape of array :', arr.shape)



# Resizing the shape of array

# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarr = arr.reshape(2,3,2)
# print(newarr)


#Numpy Array iterating

# arr = np.array([1,2,3,4,5,6])

# for x in arr:
#     print(x)


# arr = np.array([
#     [1,2,3],
#     [4,5,6]
# ])

# for x in arr:
#     print(x)


#result of this
# [1 2 3]
# [4 5 6]


# for x in arr:
#     for y in x:
#         print(y)


# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# for x in arr:
#     for y in x:
#         for z in y:
#             print(z)
   


# arr = np.array([
#     [
#         [1,2],
#         [3,4]
#     ],
#     [
#         [5,6],
#         [7,8]
#     ]
# ])

# for x in np.nditer(arr):
#     print(x)



# Joining of two arrays

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])

# arr = np.concatenate((arr1, arr2))

# print(arr)


# arr1 = np.array([
#     [1,2],
#     [3,4]
# ])

# arr2 = np.array([
#     [5,6],
#     [7,8]
# ])

# arr = np.concatenate((arr1, arr2), axis=1)
# print(arr)



# Splitting Numpy arrays

# arr = np.array([1,2,3,4,5,6])

# newarr = np.array_split(arr, 4)
# print(newarr,"index",newarr[0])


# arr = np.array([
#     [1, 2],
#     [3, 4], 
#     [5, 6], 
#     [7, 8], 
#     [9, 10], 
#     [11, 12]])

# newarr = np.array_split(arr, 3)
# print(newarr)



# Searching arrays

# arr = np.array([1,2,3,4,5,6,7,8,9, 4])
# x = np.where(arr == 4)
# print(x)

# evenindex = np.where(arr%2 == 0)
# print(evenindex)



# Sorting the arrays

# arr = np.array([1,5,2,6,4,8,9])
# print(np.sort(arr))

# arr1 = np.array(['anand', 'shalini', 'vinay', 'manoj'])
# print(np.sort(arr1))


# arr = np.array([True, False, True])
# print(np.sort(arr))


# arr = np.array([
#     [3,2,4],
#     [5,0,1]
# ])

# print(np.sort(arr))


# Filtering in arrays

# arr = np.array([41,42,43,44])

# x = [True, False, True, False]

# newarr = arr[x]

# print(newarr)


# arr = np.array([41,42,43,44])

# filter_arr = []

# for element in arr:
#     if element >42 :
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)

# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)

# Create a filter array that will return
# only even elements from the original array:

arr = np.array([1,2,3,4,5,6,7,8])

filter_arr = []

for elements in arr:
    if elements % 2 == 0:
        filter_arr.append(True)

    else:
        filter_arr.append(False)


newarr = arr[filter_arr]
print(filter_arr, newarr)
