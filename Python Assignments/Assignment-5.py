print("1. Write a program to print multiplication table.")
n=float(input("Enter a no. whose table you want to print"))
for i in range (1, 11):
    print(n,"*", i,"=" , n * i)

print("2. Write a program to compute sum of first n natural numbers.")
n=float(input("Enter a no. whose sum of first n natural numbers you want to print"))
s = 0
x = 1
while x <=n :
    s = s + x
    x = x + 1
print(s)

print("3. Write a program that prompts a number from the user and generates the Fibonacci sequence upto that number. The Fibonacci sequence is given as under: 0 1 1 2 3 5 8 13 21 43 …")
n = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
print("Fibonacci sequence:")
while count < n:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1

print("4.Write a program that prompts the user for an integer number and then prints all its factors")
x=int(input("Enter a positive integer: "))
print("Factors of ", x,"are:")
for i in range(1, x + 1):
    if x % i == 0:
        print(i)

print("5. Write a program to determine whether a number is palindrome or not.")
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

print("6. Write a program to determine whether a number is prime or not.")
num=int(input("Enter number:"))
if num > 1:
   for i in range(2, num):
       if (num % i) == 0:
           print(num, "is not a prime number")
           break
   else:
       print(num, "is a prime number")
else:
   print(num, "is not a prime number")

print("7. Write a program to determine an Armstrong number.")
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

print("8. Write a program to reverse the digits of a number.")
Number = int(input("Please Enter any Number: "))
Reverse = 0
while(Number > 0):
    Reminder = Number %10
    Reverse = (Reverse *10) + Reminder
    Number = Number //10
print("\n Reverse of entered number is = %d" %Reverse)

print("9. Write a program to compute HCF of a number input by the user.")
def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf
num1 = 54
num2 = 24
print("The H.C.F. is", compute_hcf(num1, num2))

print("10. Write a program to read n integer numbers interactively and print the biggest and smallest numbers.")
NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

print("The Smallest Element in this List is : ", min(NumList))
print("The Largest Element in this List is : ", max(NumList))
