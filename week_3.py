'''
For longer comments
'''

#int, float, bool, string same as other languages (html)

x=3
y=4.5
z=True
s="Hello"
print(x,type(x))
print(y,type(y))  
print(z,type(z))
print(s,type(s))
#You can have multiple assignments in one line using commas
a,b,c=1,2.5,False

#some function call: print, input, type, str, int, float, bool
#input always returns a string

#Converting between types
num_as_text=45
num_as_number=int(num_as_text) #convert string to number

print(num_as_text,type(num_as_text))
print(num_as_number)

num=3
num_f= float(3)

num2=4.5
num2_i=int(num2) #convert float to int (truncates)

year_of_birth=input("Enter your year of birth: ")
print("Your age is",2025-int(year_of_birth)) #convert string to int... if there is no int in the string it will crash

#ser_input=input("Please enter your year of birth: ")
#ge=2025-int(user_input)
#print("Your age is",age)

#What about if i dont want to use numbers? 
#convert to bool

sports_are_g=input("Are sports good? (Yes/No): ")
print("Your answer is",str(sports_are_g)) #any string is True except empty string

prim_color=input("Enter one of the primary colors: ")
if prim_color.lower() == "red" or prim_color.lower() == "blue" or prim_color.lower() == "yellow":
    print(prim_color,"is a primary color")
else:
    print(prim_color,"is not a primary color")
    
#Why use lower()?
#To convert the string to all lowercase letters
#So that we can compare the string without worrying about capitalization

#Print function
print("Hello","World", sep='',  end="")
#sep is what goes between the things you are printing
#end is what goes at the end of the print statement (default is newline)
print("Hello \tWorld") #\t is a tab
print("Hello \nWorld") #\n is a newline
print('What is the student\'s name?')
print('Use this symbol \\ to make an escape character') #the use of escape character is to print special characters like \n or \t


#expressions
expression = 3+4*0-300+12/3
print(expression)
#order of operations: PEMDAS
#Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
#Left to right for operations of the same precedence
#Use parentheses to change the order of operations
expression2 = (3+4)*(0-300+12)/3
print(expression2)

x = 3
x = x + 5
print(x)


#NOW WE ARE LEARNING THE "IF STATEMENT"

#"IF" is for check something

#The formula is basically 
''' if
elif
elif
else''' #Always "else" is the last one

'''If we have for example: condition = x < y and y < z it would be correct only if both are correct'''
''' "and" "or" are helpful for IF'''

#read a,b and c from the user
#if a== 0 then x1 = x2 = -c/b
#x1 = (-b +sqrt(bʌ2- 4*a*c))/(2*a) # **0.5
#x2 = (-b -sqrt(bʌ2- 4*a*c))/(a*a)
#e#lse print "No posisible solution"
#print x1, x2

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


''' what about if you have more than one option for if'''

if age <90 and age > 18:
     print("You are elegible for a driver's license.")
else: 
    print("You are not elegible for a diver's license.")
