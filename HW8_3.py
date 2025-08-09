items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

freq = {}

for item in items:
    freq[item] = freq.get(item, 0) + 1

print(freq)
