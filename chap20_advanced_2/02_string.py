print("=== Part 1 ===")
s = 'hello WORLD'
print(f'input:\t\t\t{s}')
print(f'capitalize:\t\t{s.capitalize()}')
print(f'upper:\t\t\t{s.upper()}')
print(f'lower:\t\t\t{s.lower()}')
print(f"count('l'):\t\t{s.count('l')}")
print(f"find('l'):\t\t{s.find('l')}")
print(f"center(20, '-'):\t{s.center(20, '-')}")


print("\n=== Part 2 ===")
s = 'hello'
print(f'input:\t\t\t{s}')
print(f'isalnum:\t\t{s.isalnum()}')
print(f'isalpha:\t\t{s.isalpha()}')
print(f'islower:\t\t{s.islower()}')
print(f'isupper:\t\t{s.isupper()}')
print(f'isspace:\t\t{s.isspace()}')
print(f'isnumeric:\t\t{s.isnumeric()}')
print(f'istitle:\t\t{s.istitle()}')
print(f"startswith('he'):\t{s.startswith('he')}")
print(f"endswith('lo'):\t\t{s.endswith('lo')}")
print(f"split('e'):\t\t{s.split('e')}")
print(f"partition('e'):\t\t{s.partition('e')}")