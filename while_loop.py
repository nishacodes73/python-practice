#Q.1. write a  Python program using a while loop to print numbers from 1 to 10

num=1

while num<=10:
   print(num)
   num+=1


#Q.2. Write a Python program using a while loop to print all even numbers from 2 to 20
even_num=2
print("Even numbers:")
while even_num<=20:
     print(even_num)
     even_num+=2

#Q.3.Write a program using while loop that prints numbers from 10 down to 1,then prints Blast off!
num=10
print("Reverse num from 10 to 1:")
while num>=1:
     print(num)
     num-=1
print("Blast off!")

#Q.4. Write a python program using while loop to calculate the sum of numbers from 1 to 10
num=1
total=0
while num<=10:
     total=total+num
     num+=1
print(" Sum=",total)

#Q.5. Count how many numbers are divisible by 3 from 1 to 15.
num = 1
count = 0

while num <= 15:
     if num % 3 == 0:
         count += 1
     num += 1

print("Numbers divisible by 3:", count)

#Q.6.Write a program using a while loop to print the multiplication table of 5,from 5*1 to 5*10.
num=5
i=1

while i<=10:
     mul=num*i
     print(num,"*",i,"=",mul)
     i+=1

#Q.7. Write a program using while loop that counts down from 123 to 0 by removing the last digit each time.
num=123

while num>0:
     print(num)
     num=num//10
    
print(0)

#Q.8. Write a program using a while loop to print the digits of 4321 by removing the last digit each time.
num=4321

while num>0:
     print(num)
     num=num//10

#Q.9. Write a program using a while loop to count how many digits are in num=5836
num=5836
count=0
while num>0:
     count+=1
     num=num//10

print("Number of digits:",count)

#Q.10. Write a Python program using a while loop to calculate the sum of digits of num=583.
num=583
total=0
while num>0:
     digit=num%10
     total=total+digit
     num=num//10

print("Sum of 583:",total)
