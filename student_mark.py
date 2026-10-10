# Student Marks and Grade Checker

name = input("Enter your name: ")
marks = int(input("Enter marks out of 100: "))

print("Student name:", name.upper())

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Excellent")
elif marks >= 60:
    print("Good")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
