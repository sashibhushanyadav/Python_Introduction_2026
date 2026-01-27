# List
# append, insert, extend, remove/pop, index, count, sort, reverese

x = ['a', 'b', 12, 34, 0.23, True]
y=[2,3,4]

x.append(1) # append
print(x)

x.insert(2, 's') # insert
print(x)

y.extend([0,1,'z'])  # extend
print(y)

y.remove(0) # remove - based on value
print(y)

y.pop(2) # pop - it removes based on index
print(y)

a = [0,2,5,3,2,0,2,3,2,]

idx = a.index(5) # .index(item, [start], [end]) - Returns index of first occurrence
print(idx)

count = a.count(2) # it counts the value
print(count)

z = ['sashiii', 'rajeev', 'dhiraj', 'rajan']

z.sort() # sorting in an ascending order
print(z)

z.sort(reverse=True) # sorting in an descending order
print(z)

z.reverse() # sorting in an descending order
print(z)

z.sort(key=len) # sorting based on length
print(z)

original = [3, 4, 5, 2]
new_list = original.copy()
print(new_list)




