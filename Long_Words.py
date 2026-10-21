words = ["apple", "cat", "python", "book", "programming"]
n = 4
result = []

for word in words:
    if len(word) > n:
        result.append(word)

print("Words longer than", n, ":", result)
