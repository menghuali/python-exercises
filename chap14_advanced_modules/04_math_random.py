import math
import random


def math_1(num) -> None:
    print(f'\nFloor, Ceil, and Round of {num}')
    print(f'floor\t: {math.floor(num)}')
    print(f'ceil\t: {math.ceil(num)}')
    print(f'round\t: {round(num)}')  # round to even number


math_1(4.37)
math_1(4.5)
math_1(5.51)
math_1(5.5)


def math_2():
    print('\nMatch constants')
    print(f'pi\t\t: {math.pi}')
    print(f'e\t\t: {math.e}')
    print(f'inf\t\t: {math.inf}')
    print(f'inf > 10**20\t: {math.inf > 10**100}')
    print(f'nan\t\t: {math.nan}')


math_2()


def math_3():
    print('\nCommon math functions')
    print(f'log(e)\t\t: {math.log(math.e)}')
    print(f'log(10, 100)\t: {math.log(100, 10)}')
    print(f'sin(pi/2)\t: {math.sin(math.pi/2)}')
    print(f'degrees(pi)\t: {math.degrees(math.pi)}')
    print(f'radians(180)\t: {math.radians(180)}')


math_3()


def randmon_int():
    print('\nRandom 20 numbers between 0 and 100')
    print([random.randint(0, 100) for n in range(0, 20)])


randmon_int()


def random_seed():
    random.seed(101)
    array = [random.randint(0, 100) for n in range(0, 20)]
    random.seed()
    return array


print('\nRandom 20 numbers between 0 and 100, with seed. Every time you will get same series of randmon numbers.')
print(f'#1: {random_seed()}')
print(f'#2: {random_seed()}')
print(f'#3: {random_seed()}')


def randmon_choice():
    array = list(range(0, 20))
    print(
        f'\nRandomly pick up 1 element from array {array}\t: {random.choice(array)}')
    print(
        f'Randomly pick up 10 elements from array {array}\t: {random.choices(population=array, k=10)}')


randmon_choice()


def random_sample():
    array = list(range(0, 20))
    print(
        f'\nRandomly pick elements from array {array}, no repeats: {random.sample(population=array, k=10)}')


random_sample()


print(f'\nrandom.uniform: {[random.uniform(0, 100) for x in range(0, 20)]}')
print(
    f'\nrandom.gauss (normal distribution): {[random.gauss(mu=0, sigma=1) for n in range(0, 50)]}')
