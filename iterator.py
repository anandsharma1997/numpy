

class SimpleIterator :
    def __iter__(self):
        self.current = 0
        return self
    
    def __next__(self):
        if self.current < 5:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration
        


iterator = SimpleIterator()

for num in iterator :
    print("first",num)





list = [1, 2, 3, 4, 5, 6]

iteration = iter(list)
print(iteration)
print(next(iteration))