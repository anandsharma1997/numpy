

sett = {1, 2, 3, 4, 5}
set1 = {6, 7, 8}

print(type(set))

sett.add(6)
print(set)

sett.remove(6)
print(set)

union_set = sett.union(set1)
print(union_set)

intersection_set = set.intersection(set1)

print(intersection_set, "intersaction")


even_square = {x**2 for x in range(1,11) if x %2 == 0}

print(even_square)

to_be_set = {1, 2, 3, 4}

frozen_set = frozenset(to_be_set)

print(type(frozen_set))

#set difference

set3 = {1, 2, 3}
set4 = {3, 4, 5}

difference_Set = set3.difference(set4)
print(difference_Set)



set5 = {1, 2, 3}
set6 = {1, 2, 3, 4, 5, 6}

is_subset = set5.issubset(set6)
is_superset = set6.issuperset(set5)

print(is_subset, is_superset)



