print("Which of the following expressions are true or false?")
print("i) 10 != 15 and not(7<12) or 34<57")
print(10 != 15 and not(7<12) or 34<57)

print("ii) 10 + 10 == 20 or 2 + 6 = 8")
print(10 + 10 == 20 or 2 + 6 or 8)

print("iii) 5 + 6 == 12 and 4 * 3 == 12")
print( 5 + 6 == 12 and 4 * 3 == 12)

print("iv) 11 < 15  and 54 > 50 or 52-10 <= 42")
print(11 < 15  and 54 > 50 or 52-10 <= 42)

print("\nDetermine the value of each of the following expression if a=7, b=3, and c=-2")
a=7
b=3
c=-2
print("a. b >15 and c < 0 or a > 0")
a2= (b >15 and c < 0 or a > 0)
print("The result of a.) is" ,a2)
b2= (a == c or b > a)
print("The result of b.) is" ,b2)
c2= (a > b and b > c)
print("The result of c.) is" ,c2)
d2= ((a - b) > (c + a))
print("The result of d.) is" ,d2)
e2= (a * c)
print("The result of e.) is" ,e2)

print("Write a program to compute the area of the following two dimensional shapes")
print("i.) Circle")
PI = 3.14
rc = float(input(' Please Enter the radius of a circle: '))
areac = PI * rc * rc
print("Area of the circle is ",areac )

print("\nii.) Triangle")
a = float(input('Please Enter the First side of a Triangle: '))
b = float(input('Please Enter the Second side of a Triangle: '))
c = float(input('Please Enter the Third side of a Triangle: '))
s = (a + b + c) / 2
Areat = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The Area of a Triangle is", Areat)

print("\niii.) Rectangle")
widthr = float(input('Please Enter the Width of a Rectangle: '))
heightr = float(input('Please Enter the Height of a Rectangle: '))
Arear = widthr * heightr
print("Area of a Rectangle is:", Arear)

print("\niv.) Square")
sides = float(input('Please Enter the Side of a Square: '))
areas=sides*sides
print("Area of a Square is:", areas)

print("\nv.) Trapezoid")
bs1 = float(input('Please Enter the First Base of a Trapezoid: '))
bs2 = float(input('Please Enter the Second Base of a Trapezoid: '))
heightt = float(input('Please Enter the Height of a Trapezoid: '))
AreaT = 0.5 * (bs1 + bs2) * heightt
print("Area of a Trapezium = ", AreaT)

print("\nvi.) Sphere")
radius = float(input('Please Enter the Radius of a Sphere: '))
sa =  4 * PI * radius * radius
print("The Surface area of a Sphere =",sa)

print("\nvii.) Parallelogram")
basep = float(input('Please Enter the Base of the Parallelogram: '))
heightp = float(input('Please Enter the Height of a Parallelogram: '))
ap = basep * heightp
print("The Surface area of a Sphere =" ,ap)

print("Write a program to compute volume of the following three dimensional shapes")
print("i.) Cube")
l = float(input('Please Enter the Length of any Side of a Cube: '))
Volume = l * l * l
print(" Volume of cube = " ,Volume)

print("ii.) Cylinder")
PI=3.14159
radiusC = float(input('Please Enter the Radius of a Cylinder: '))
heightC = float(input('Please Enter the Height of a Cylinder: '))
VolumeC = PI * radiusC * radiusC * heightC
print(" The Volume of a Cylinder = " ,VolumeC)

print("iii.) Cone")
radiusCo = float(input('Please Enter the Radius of a Cone: '))
heightCo = float(input('Please Enter the Height of a Cone: '))
VolumeCo = PI * radiusCo * radiusCo * (heightCo/3)
print(" The Volume of a Cylinder = " ,VolumeCo)


print("\n\nChlo by bhaion baki ka timepass adme.........  ;)")
