print("Welcome to the quadratic equation solver")
import math
# Read a, b, and c from the user
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a == 0:
    if b != 0:
        x1 = x2 = -c / b
        print("x1 =", x1, "x2 =", x2)
    else:
        print("No possible solution")
else:
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        print("No real solutions")
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        print("x1 =", x1, "x2 =", x2)
2





