
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
print('Use this symbol \\ to make an escape character')