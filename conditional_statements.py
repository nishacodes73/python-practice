# Python Conditional Statements
# Topics: if, elif, and else

marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks. Enter marks between 0 and 100.")
elif marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")

print("Program completed.")
