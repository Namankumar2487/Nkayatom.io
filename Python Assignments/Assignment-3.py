import math
print("Q1. Write a program to compute square of a number.")
n = float(input(" Please Enter the no. whose sq u want to calculate : "))
sq = n * n
print("The Square is ",sq)

print("Q2. Write a program to compute square root of a number..")
no = float(input(" Please Enter the no. whose squareroot u want to calculate : "))
sqroot = math.sqrt(no)
print("The Square Root of a Given Number ",sqroot)

print("Q3. Write a program to compute simple interest and compound interest.")
p = float(input("Enter the principal"))
r = float(input("Enter the rate of interest"))
t = float(input("Enter the time period"))
si = (p * t * r)/100
print('The Simple Interest is', si)

print("Q4. Write a program to compute total cost where number of units and price per unit are input by user.")
price = float(input("Enter the price per unit:"))
units = float(input("Enter the no. of units"))
tc=price*units
print('The total cost is', tc)

print("Q5.Write a program to compute sum, subtraction, multiplication,division and exponent of given variables input by the user.")
a = float(input("Enter the first no.:"))
b = float(input("Enter the second no.:"))
print("Sum: ",a+b)
print("Sub: ",a-b)
print("Mul ",a*b)
print("Divide ",a/b)
print("Exponent ",a**b)

print("Q6.Write a program to compute distance between two points.")
x1=int(input("Enter the x cordinate for 1st point : "))
x2=int(input("Enter the x cordinate for 2st point :"))
y1=int(input("Enter the y cordinate for 1st point :"))
y2=int(input("Enter the y cordinate for 2st point :"))
result= ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)
print("distance between",(x1,x2),"and",(y1,y2),"is : ",result)

print("Q7.Write a program to compute slope of a line.")
x1=int(input("Enter the x cordinate for 1st point : "))
x2=int(input("Enter the x cordinate for 2st point :"))
y1=int(input("Enter the y cordinate for 1st point :"))
y2=int(input("Enter the y cordinate for 2st point :"))
result= (y2-y1)/(x2-x1)
print("Slope of the 2 points",(x1,x2),"and",(y1,y2),"is : ",result)

input()
