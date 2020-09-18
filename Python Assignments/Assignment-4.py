print("Q1. Write a program to print largest of three numbers using if-else statement.")
a = float(input("Please Enter the First value: "))
b = float(input("Please Enter the Second value: "))
c = float(input("Please Enter the Third value: "))
if (a > b and a > c):
          print("{0} is Greater Than both {1} and {2}". format(a, b, c))
elif (b > a and b > c):
          print("{0} is Greater Than both {1} and {2}". format(b, a, c))
elif (c > a and c > b):
          print("{0} is Greater Than both {1} and {2}". format(c, a, b))
else:
          print("Either any two values or all the three values are equal")

print("Q2. Write a program to determine whether a year is leap or not.")
x=int(input("Enter the year:"))
if ((x%400)==0 or ((x%4) == 0) and ((x%100)!=0)):
    print("%d is a Leap Year" %x)
else:
    print("%d is Not the Leap Year" %x)

print("Q3. Write a program to determine whether a number is even or odd.")
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("No. is Even",num)
else:
   print("No. is Odd",num)

print("Q4. Write a program to determine whether a triangle is isosceles or not?")
a = float(input("Please Enter the First Side: "))
b = float(input("Please Enter the Second Side: "))
c = float(input("Please Enter the Third Side: "))
if(a == b or a == c or b == c):
        {
            print("It's an Isosceles Triangle\n")
        }
else:
        {
            print("It's not a isosceles Triangle\n")
        }

print("5. Write a program to find out the roots of a quadratic equation.")
a = int(input("Please Enter a Value of a Quadratic Equation : "))
b = int(input("Please Enter b Value of a Quadratic Equation : "))
c = int(input("Please Enter c Value of a Quadratic Equation : "))

discriminant = (b * b) - (4 * a * c)

if(discriminant > 0):
    root1 = (-b + math.sqrt(discriminant) / (2 * a))
    root2 = (-b - math.sqrt(discriminant) / (2 * a))
    print("Two Distinct Real Roots Exists: root1 = %.2f and root2 = %.2f" %(root1, root2))
elif(discriminant == 0):
    root1 = root2 = -b / (2 * a)
    print("Two Equal and Real Roots Exists: root1 = %.2f and root2 = %.2f" %(root1, root2))
elif(discriminant < 0):
    root1 = root2 = -b / (2 * a)
    imaginary = math.sqrt(-discriminant) / (2 * a)
    print("Two Distinct Complex Roots Exists: root1 = %.2f+%.2f and root2 = %.2f-%.2f" %(root1, imaginary, root2, imaginary))

print("6. Write a program to print numbers upto N which are not divisible by 3 , 6, and 9, e.g., 1, 2, 4, 5, 7, …")
n = int(input("Please Enter the no. of integers u want to display: "))
for i in range(1,n+1):
    if i%3 != 0:
        print(i)
