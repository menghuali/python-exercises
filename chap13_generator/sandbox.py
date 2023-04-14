def create_cubes(n):

    for x in range(n):
        yield x ** 3


print("Cubes...")
for c in create_cubes(10):
    print(c)

print('\nFibonacci...')


def fibonacci(n):

    a = 1
    b = 1
    for x in range(n):
        yield a
        a, b = b, a + b


for n in fibonacci(10):
    print(n)

print('\nIterating Fibonacci genarator...')
f_iter = fibonacci(3)
print(next(f_iter))
print(next(f_iter))
print(next(f_iter))

s = 'Hello World'
print("\nIterating string '{s}'")
s_iter = iter(s)
next(s_iter)
next(s_iter)
