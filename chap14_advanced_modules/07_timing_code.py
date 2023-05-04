import timeit

timespan = timeit.timeit(stmt='func(100)', setup='''
def func(n):
    return [str(x) for x in range(n)]
''', number=1000000)
print(f'function 1: {timespan}')

timespan = timeit.timeit(stmt='func(100)', setup='''
def func(n):
    return list(map(str, range(n)))
''', number=1000000)

print(f'function 2: {timespan}')
