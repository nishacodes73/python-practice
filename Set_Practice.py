# Python Set Practice

# 1. Create a set
numbers = {10, 20, 30, 40, 20, 10}
print("Original Set:", numbers)

# 2. Find the number of unique elements
print("Number of Elements:", len(numbers))

# 3. Add an element
numbers.add(50)
print("After Adding 50:", numbers)

# 4. Remove an element
numbers.remove(20)
print("After Removing 20:", numbers)

# 5. Check whether an element exists
print("Is 30 present?", 30 in numbers)

# 6. Set Operations
set_a = {10, 20, 30, 40}
set_b = {30, 40, 50, 60}

print("Intersection:", set_a.intersection(set_b))
print("Union:", set_a.union(set_b))
print("Difference:", set_a.difference(set_b))