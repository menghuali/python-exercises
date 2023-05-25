l = [1, 2, 2, 3, 4, 5, 5]
print(l.count(5))

x = ['y', 'x', 'z']

l.extend(x)
print(l)

print(l.index(2))
# print(l.index(-1))

l.insert(2, 'w')
print(l)

print(l.pop())
print(l)
print(l.pop(0))
print(l)

l.remove(5)
print(l)

l.reverse()
print(l)

l2 = [9, 8, 7, 6, 5]
l2.sort()
print(l2)
