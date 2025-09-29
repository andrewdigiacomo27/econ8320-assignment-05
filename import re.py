




import re

mystring = "261 S 800 E\nSalt Lake City, UT 84102"

results = re.search(r'(\w+(?: \w+)*)(?:, )([A-Z]{2})', mystring).groups()
print(results[0])
print(results[1])