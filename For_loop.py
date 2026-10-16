# Write a python program using a for loop to print the numbers from 1 to 10,each on a new line.
for i in range(1,11):
    print(i)

#print all even numbers from 2 to 20.
for i  in range (2,22,2):
    print(i)

# calculate the sum of numbers from 1 to 10 and print the final sum
n=10
sum=0
for i in range(1,11):
    sum+=i

print ("Final sum:",sum)

# Print the multiplication table of 7 ,from 7*1 to 7*10.
n=7
for i in range(1,11):
    mul=n*i
    print(n,"*",i,"=",mul)

# WAP to count how many vowels are in this word
word="education"
count=0
for i in word:
    if i in "aeiou":
        count +=1

print("Numbers of vowels",count)

# Find the largest number in this list
numbers=[12,45,7,89,23]
largest=numbers[0]
for i in numbers:
    if i>largest:
        largest=i
print("Largest number:",largest)

#count positive numbers
numbers=[5,-2,8,-1,0,12]
count=0
for i in numbers:
    if i>0:
        count+=1
print("Positive numbers:",count)