
# create a list of lengths of words in a given sentece using a list comprsion and the len method function

sentence = "My name is anand sharma"

word_lengths = [len(word) for word in sentence.split()]

print(word_lengths)


numbers = [num**2 for num in range(1,10) if num**2 > 10]
print(numbers)


list1 = [1, 2, 3]
list2 = [4, 5, 6]

sum_list = [a + b for a, b in zip(list1, list2)]

print(sum_list)

