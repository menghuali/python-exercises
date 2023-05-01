import re


text = "The agent's phone number is 408-555-1234. Call this number soon!"


def basic_regex_func():
    print(f"No match: {re.search(pattern='NOT IN TEXT', string=text)}")

    match = re.search('number',  text)
    print(f'\nsearch\t\t: {match}')
    print(f'match.start\t: {match.start()}')
    print(f'match.end\t: {match.end()}')

    matches = re.findall('number', text)
    print(f'\nfindall: {matches} (element type: {type(matches[0])})')

    it = re.finditer('number', text)
    print(f'\nIterating matches: {[m for m in it]}')

    it = re.finditer('number', text)
    print(f'\nIterating and convert matches to str: {[m.group() for m in it]}')


print('=== Part 1: Basic Regex Functions ===\n')
basic_regex_func()


def regex_1():
    phone_pattern = r'\d{3}-\d{3}-\d{4}'
    print(f'\n{phone_pattern}\t: {re.search(phone_pattern, text)}')

    # group
    phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
    result = re.search(phone_pattern, text)
    print(f'group()\t\t\t: {result.group()}')
    print(f'group(1)\t\t: {result.group(1)}')
    print(f'group(2)\t\t: {result.group(2)}')
    print(f'group(3)\t\t: {result.group(3)}')


print('\n\n=== Part 2: Basic Regex ===')
regex_1()


def findall(pattern, text):
    print(f'{pattern} ==> {text} ==> {re.findall(pattern, text)}')


def regex_2():
    findall(r'dog|cat', 'There is a dog')
    findall(r'dog|cat', 'There is a cat')
    findall(r'.{3}at', 'The cat in the hat went splat')
    findall(r'^\d', '1 is a number')
    findall(r'^\d', 'One is a number')
    findall(r'\d$', 'The number is 1')
    findall(r'\d$', 'The number is one')
    findall(r'[^\d]+', 'There are 3 numbers 34 inside 5 this sentence')
    findall(r'[^.!?\s]+', 'This is a string! But it has punctuation. How to remove it?')
    findall(r'[\w]+-[\w]+', 'Only find the hypen-words in this sentence. But you do not know how long-ish they are.')
    cat_pattern = r'cat(fish|nap|erpillar)'
    findall(cat_pattern, 'Hello, would you like some catfish?')
    findall(cat_pattern, 'Hello, would you like to take a catnap?')
    findall(cat_pattern, 'Hello, have you seen this caterpillar?')

print('\n\n=== Part 3: More Regex ===\n')
regex_2()
