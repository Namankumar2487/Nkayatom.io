print("Q.1 Identify the data type that appropriately describes the data given below:")
print('Answer of Question No.1 is')
a = 32.e10
print(type(a))
b = -8.56e100
print(type(b))
c = 34.j
print(type(c))
d = -876
print(type(d))
e = 432
print(type(e))
f = 4375457
print(type(f))
print("f = 4375457L print(type(g)) Will generate an Error Because long is no longer used in python3.0 and upper versions instead use 4375457")

print("\nQ.2 Initialize a list with heterogeneous values then use slicing operator to fetch and print different values.")
List =list(range(1, 15))
print ("The List we made for our operations is", List)

#  below list has numbers from 1 to 5
List_5 = List[0 : 5]
print ("Lets print from 0 to 5", List_5)

#  below list has numbers from 6 to 8
List5_8 = List[5 : 8]
print (List5_8)

#  below list has numbers from 1 to 10
List1_ = List[0 : ]
print (List1_)

#  below list has numbers from 1 to 5
List_5 = List[: 5]
print (List_5)

#  below list has numbers from 2 to 8 in step 2
List1_8_2 = List[1 : 8 : 2]
print (List1_8_2)

#  below list has numbers from 10 to 1
List_rev = List[ : : -1]
print (List_rev)

#  below list has numbers from 10 to 6 in step 2
List_rev_9_5_2 = List[9 : 4 : -2]
print (List_rev_9_5_2)

print("\nQ.3 Practice set data type use and print its values.")
set = {'Hello', 2, 3,'Python','Nothing special to do for now',6,'Set is unordered data type'}
print(set)

print("\nQ.4 Practice dictionary data type use and print its values.")
RR = {
  "brand": "RolceRoyce",
  "model": "Ghost",
  "year": 2012
}
print(RR)
print('Get the value of the "model" key: ')
x = RR["model"]
print("Change the year to 2020: ")
RR = {
  "brand": "RolceRoyce",
  "model": "Ghost",
  "year": 2012
}
RR["year"] = 2020

#Just another way of doing operations on dictionary
for x, y in RR.items():
  print(x, y)

print("\nQ.5 Input a number and print its value.")
inp = input("Enter the value you want to display: ")
print(inp)

print ("\nQ.6. Practice various output formatting options in python.")
print("Learning Python")
print("Python","Basics","Timepass")
n=10
print(n)
#print variable with string message
age=input("Enter Your Age")
print("Your Age is",age)
print("Hello, You Are ",age,"Years Old")

print("Easy","Python","Tutorial")
print("Easy","Python","Tutorial",sep='-')
print("Easy","Python","Tutorial",sep='@')
print("Python",end='\n')
print("Python",end='\t')
print("Python",end='-')

print("\nThanks, That's all for now, we will continue in next assignment")

input("\nPress 'Enter' if u want to end the program")
