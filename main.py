import pyttsx3
import numpy as np
from setuptools import setup
import os
import PyQt5


def cbrt(): #Function to find cube root
    num=float(input("Enter a number "))
    cube_root = np.cbrt(num)
    print("The cube root of the number is: ",cube_root)
  

def sqrt(): #Function to find square root
    num = float(input("Enter the number: "))
    square_root = np.sqrt(num)
    print("The square root of the number is ",square_root)
  

def trig(): #Function to find trigonometric functions
    angle = float(input("Enter the angle (in degrees): "))
    choice = int(input("1. sin \n2. cos \n3. tan\nWhat do you want to take out? "))
    sin = np.sin(angle) 
    cos = np.cos(angle)
    tan = np.tan(angle)

    if choice == 1:
        print("The sine of the angle is: ",sin)
    elif choice == 2:
        print("The cosine of the angle is: ",cos)
    elif choice == 3:
        print("The tangent of the angle is: ",tan)
    else:
        print("Sorry, probably you have made a mistake. \nNote: We do not support inverse trignometric functions.")

def log(): #Function to find logarithm
    num = float(input("Enter a number: "))
    norten = str(input("What do you want to take out? \n1. Natural log \nLog Base 10 \nLog Base 2"))
    logn = np.log(num)
    log10 = np.log10(num)
    log2 = np.log2(num)

    if norten == 1 or str("Natural log"):
        print("The natural log of the number is ",logn)
    elif norten == 2 or str("Log Base 10"):
        print("The log of the base 10 number is ",log10)
    elif norten == 3 or str("Log Base 2"):
        print("The log of the base 2 number is ",log2)

def factorial(): #Function to find factorial
    num = int(input("Enter a number: "))
    ftrl = np.factorial(num)
    print("The factorial of the number is ",ftrl)

def twod(): #Function to find area and perimeter

    area_or_perimeter = int(input("1. Area \n2. Perimeter\nWhat do you want to find? "))

    if area_or_perimeter == 1:
        print("1. Square \n2. Rectangle \n3. Circle \n4. Parallelogram \n5. Rhombus")
        figure = int(input("Which figure? "))
        if figure == 1:
            side = float(input("Side length: "))
            area = side * side
            print("The area of the square is ",area)

        elif figure == 2:
            length = float(input("Length: "))
            breadth = float(input("Breadth: "))
            area = length * breadth
            print("The area of the rectangle is: ",area)

        elif figure == 3:
            radius = float(input("Radius: ")) 
            area = np.pi * radius * radius
            print("The area of the circle is ",area)

        elif figure == 4:
            base = float(input("Base: "))
            height = float(input("Height: "))
            area = base * height
            print("The area of the parallelogram is ",area)

        elif figure == 5:
            d1 = float(input("First diagonal: "))
            d2 = float(input("Second diagonal: "))
            area = (d1 * d2)/2
            print("The area of the rhombus is: ",area)

    elif area_or_perimeter == 2:
        print("1. Square \n2. Rectangle \n3. Circle (Circumference) \n4. Parallelogram \n5. Rhombus")
        figure = int(input("Which figure? "))
        
        if figure == 1:
            side = float(input("Side length: "))
            perimeter = 4 * side
            print("The perimeter of the square is ",perimeter)

        elif figure == 2:
            length = float(input("Length: "))
            breadth = float(input("Breadth: "))
            perimeter = 2*(length+breadth)
            print("The perimeter of the rectangle is: ",perimeter)

        elif figure == 3:
            radius = float(input("Radius: ")) 
            perimeter = 2 * np.pi * radius
            print("The perimeter of the circle is ",perimeter)

        elif figure == 4:
            base = float(input("Base: "))
            side = float(input("Side: "))
            perimeter = 2*(base+side)
            print("The perimeter of the parallelogram is ",perimeter)

        elif figure == 5:
            side = float(input("Side: "))
            perimeter = 4 * side
            print("The perimeter of the rhombus is: ",perimeter)

    else:
        print("Invalid Input")  

def threed(): #Function to find surface area and volume
    sa_v = int(input("1. Surface Area \n2. Volume\nWhat would you like to calculate? "))

    if sa_v == 1:
        shape = int(input("1. Cube \n2. Cuboid \n3. Cylinder \n4. Cone\n5. Sphere\nWhich shape? "))
        if shape == 1:
            side = float(input("Enter side length: "))
            SA = 6 * side * side
            print("The surface area of the cube is ",SA)

        elif shape == 2:
            l = float(input("Length: "))
            b = float(input("Breadth: "))
            h = float(input("Height: "))
            SA = 2*((l*h)+(b*h)+(b*l))
            print("The surface area of the cuboid is: ",SA)

        elif shape == 3:
            r = float(input("Radius: "))
            h = float(input("Height: "))
            SA = (np.pi * r * r * 2) + (2 * np.pi * r * h) 
            print("The surface area of the cylinder is ",SA)

        elif shape == 4:
            r = float(input("Radius: "))
            h = float(input("Height: "))
            SA = np.pi * r * (r+np.sqrt((h ** 2)+(r ** 2))) #SA of cone = pi*r(r+sqrt(h^2+r^2))
            print("The surface area of the cone is ",SA)

        elif shape == 5:
            r = float(input("Radius: "))
            SA = 4 * np.pi * (r ** 2)
            print("The surface area of the sphere is ",SA)

        else:
            print("Invalid Input")

    elif sa_v == 2:
        shape = int(input("1. Cube \n2. Cuboid \n3. Cylinder \n4. Cone\n5. Sphere\nWhich shape? "))
        if shape == 1:
            side = float(input("Enter side length: "))
            V = side ** 3
            print("The volume of the cube is ",V)

        elif shape == 2:
            l = float(input("Length: "))
            b = float(input("Breadth: "))
            h = float(input("Height: "))
            V = l*b*h
            print("The volume of the cuboid is: ",V)

        elif shape == 3:
            r = float(input("Radius: "))
            h = float(input("Height: "))
            V = np.pi * (r ** 2) * h
            print("The volume of the cylinder is ",V)

        elif shape == 4:
            r = float(input("Radius: "))
            h = float(input("Height: "))
            V = np.pi * (r ** 2) * (h/3)
            print("The volume of the cone is ",V)

        elif shape == 5:
            r = float(input("Radius: "))
            V = (4/3) * np.pi * (r ** 3)
            print("The volume of the sphere is ",V)

        else:
            print("Invalid Input")

def power(): #Function to find the value of nth power of a number
    num = float(input("Base: "))
    power = float(input("Exponent: "))
    result = num ** power
    print("The result is: ",result)

def complexmultiply():
    print("Warning! Instead of i use j as the imaginary unit")
    complex_num1 = input("Enter a complex number: ")
    complex_num2 = input("Enter another complex number: ")
    complex_num1 = complex(complex_num1)
    complex_num2 = complex(complex_num2)
    result = complex_num1 * complex_num2
    print(result)

#Make a list from which the user can choose the operation, subsequently will follow running the associated function
#print("Welcome to QuickQuackCalc")
#print("1. Cube root \n2. Square root")
#operation = str(input("What do you want to find? "))

#Quack will be added to the name later on when we introduce "duck" features

print("Welcome to QuickQuirkyCalc")
op = int(input("1. Find area and perimeter \n2. Find volume and surface area\n3. Find square root \n4. Find Cube root \n5. Raise a number to an exponent \n6. Find factorial \n7. Find logarithm \n8. Find values of non-inverse trigonometric functions \n9. Exit\n10. Complex Number Multiplication \nWhat would you like to do? "))

def options():
 if op == 1:
     twod()
 elif op == 2:
     threed()
 elif op == 3:
     sqrt()
 elif op == 4:
     cbrt()
 elif op == 5:
     power()
 elif op == 6:
     factorial()
 elif op == 7:
     log()
 elif op == 8:
     trig()
 elif op == 9:
     exit()
 elif op == 10:
     complexmultiply()
 else:
     u = input(("Invalid input. Input R to restart "))
     if u == str("R"):
        options()
     else:
         print("Invalid input")



options()

#Elmo will dance for Asha ma'am




      


     
