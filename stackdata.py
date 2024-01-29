# stack =[]

# def pushmethod():
#     inputdata = input("Add element to the stack")
#     stack.append(inputdata)
#     print(stack)


# def popmethod():
#     if not stack:
#         print("stack is empty, nothing to pop")

#     else:
#         stack.pop()
#         print("last element removed")
#         print(stack)

# stepdata = int(input("what operation you want, 1 for adding, 2 for removing, 3 for nothing"))

# while True:

#   if stepdata ==1:
#     pushmethod()
#   elif stepdata ==2:
#     pushmethod()
#   elif stepdata == 3:
#      break
#   else:
#     print("operation ended", stack)

test = [2, 7, 11, 15]
target = 9

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if target - nums[i] == nums[j]:
                return [i,j]


twoSum(test, target )

