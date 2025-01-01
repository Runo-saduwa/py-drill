
my_set = {1, 2, 3, 4, 5, 1, 2}

print(my_set)

# loop through

for i in my_set:
  print(i)

# remove a value from a set
my_set.discard(2)
print(my_set)

# remove all elememts from a set
my_set.clear();
print(my_set)

# add to a set
my_set.add(8)
print(my_set)

# add more than one value to a set
my_set.update([7,8,0])
print(my_set)

# tuples

my_tuple = (1, 2, 3, 4, 5,)
print(my_tuple)