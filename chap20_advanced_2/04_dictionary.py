d = {'k1': 1, 'k2': 2}


print('=== comprehension ===')
d2 = {x: x**2 for x in range(10)}
print(d2)

d2 = {k: v * 100 for k, v in zip(['a', 'b'], range(2))}
print(d2)

print('=== iterate ===')
for k, v in d:
    print(f'{k}: {v}')

for k in d.keys():
    print(k)

for v in d.values():
    print(v)

for i in d.items():
    print(i)
