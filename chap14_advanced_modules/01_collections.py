from collections import Counter, defaultdict, namedtuple

print('\n\n=== Counter ===')
print(Counter([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]))
print(Counter(['a', 'a', '1', 'a', 1, 'b', 2, 'b', 2, 2]))
print(Counter('aaabbbccc1a1a3e3e4545'))
print(Counter('How many times does each workd show up in this setence with a word'.split()))

print('\nCommon Patterns of Counter')
c = Counter('aaabbbccc1a1a3e3e4545')
print(f'Get all items\t\t: {c.items()}')
print(f'Most 3 common items\t: {c.most_common(3)}')
print(f'Least 3 common items\t: {c.most_common()[:-3-1:-1]}')
print(f'Counts of each items\t: {c.values()}')
print(f'Covert to set\t\t: {set(c)}')
print(f'Convert to dictionary\t: {dict(c)}')
c.clear()
print(f'Counter cleared\t\t: {c.items()}')

print('\n\n=== Default Dictionary ===')
normal_dict = {'a': 1, 'b': 2, 'c': 3}
print(f'Normal dictionary\t\t: {normal_dict}')
try:
    normal_dict['d']
except Exception as e:
    print(f"Value of inexist key 'd'\t: {type(e)}: {e}")

default_dict = defaultdict(lambda: 0)
default_dict['a'] = 1
default_dict['b'] = 2
default_dict['c'] = 3
print(f'\nDefault dictionary\t\t: {default_dict}')
print(f"Value of inexist key 'd'\t: {default_dict['d']}")

print('\n\n=== Named Tuple ===')
Dog = namedtuple('Dog', ['age', 'breed', 'name'])
sam = Dog(age=10, breed='Husky', name='Sam')
print(f'Dog (named tuple)\t: {sam}')
print(f'Dog.age\t\t\t: {sam.age}')
print(f'Dog.breed\t\t: {sam.breed}')
print(f'Dog.name\t\t: {sam.name}')
