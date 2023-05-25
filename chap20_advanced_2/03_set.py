s = set()

s.add(1)
s.add(2)
s.add(2)
print(s)

s.clear()
print(s)

s = {1, 2, 3}
print(s)
sc = s.copy()
print(sc)

sc.add(4)
print(s)
print(sc)

s = {1, 2, 3}
s2 = {1, 2, 4}
print(s.difference(s2))
s.difference_update(s2)
print(s)

s = {1, 2, 3}
s.discard(3)
print(s)

s = {1, 2, 3}
s.discard(12)
print(s)

s = {1, 2, 3}
s2 = {1, 2, 4}
print(s.intersection(s2))

s.intersection_update(s2)
print(s)

s1 = {1, 2, 3}
s2 = {1, 2, 4}
s3 = {5}
print(s1.isdisjoint(s3))
print(s1.isdisjoint(s2))

s1 = {1, 2, 3, 4}
s2 = {1, 2}
print(s2.issubset(s1))
print(s1.issuperset(s2))
print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)
print(s1)

s1 = {1, 2}
s2 = {2, 3}
print(s1.union(s2))
print(s1)
print(s2)
s1.update(s2)
print(s1)