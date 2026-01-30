
x = {9, 2, 1, 90, 23}

x.add(11) # just add one element at the last
print(x)

x.remove(90) # remove
print(x)

x.discard(10) # remove but not sure the given value/element exists or not
print(x)

x.pop() # remove the first element
print(x)

x.clear() # empty the set
print(x)

x.update({4, 5, 1, 0, 3, 2, 1}) # it adds multiple elements (from list, tuple, set, etc.)
print(x)

y = {6, 2, 7}

# Set Operations
print(x.union(y)) # union
print(x.intersection(y)) # intersection
print(x.difference(y)) # difference (subtraction 'x-y')
print(x.symmetric_difference(y)) # difference + Union

#set Comparison Methods

a = {9, 8, 3, 4}
b = {3, 4}
c = {0, 1}

print(a.issubset(b)) 
print(b.issubset(a)) # all the elements of b lies in a = True

print(a.issuperset(b)) # some elements of a are in b and some ain't = True
print(b.issuperset(a))

print(a.isdisjoint(b))
print(b.isdisjoint(a))
print(b.isdisjoint(c)) # none of elements are matched or lied = True

