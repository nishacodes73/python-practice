numbers = [1, 2, 2, 3, 4, 4]
unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

print("List without duplicates:", unique)
