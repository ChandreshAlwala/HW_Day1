data = {
    'a': [1, 2],
    'b': [3, 4],
    'c': [5, 6]
}

flattened = []

for value_list in data.values():
    for item in value_list:
        flattened.append(item)

print(flattened)
