# Python Dictionary Practice

# 1. Create a dictionary
student = {
    "name": "Amit",
    "age": 12,
    "eng": 77,
    "maths": 85
}

# 2. Print the dictionary
print("Student Details:", student)

# 3. Access a value using its key
print("Student Name:", student["name"])

# 4. Find the number of items
print("Length:", len(student))

# 5. Display all keys
print("Keys:", student.keys())

# 6. Display all values
print("Values:", student.values())

# 7. Display all key-value pairs
print("Items:", student.items())

# 8. Print keys and values using a loop
print("\nStudent Details One by One:")
for key, value in student.items():
    print(key, ":", value)

# 9. Update the dictionary
student.update({"age": 13, "science": 90})
print("\nUpdated Dictionary:", student)

# 10. Create a dictionary using fromkeys()
subjects = ["English", "Maths", "Python"]
marks = dict.fromkeys(subjects, 0)
print("\nSubject Marks:", marks)

# 11. Clear the dictionary
student.clear()
print("\nAfter Clear:", student)