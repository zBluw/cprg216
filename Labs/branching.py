input("Enter something: ") #It has a user provided value
age=2025 - 1990 #It has a calculated value

#boolean values
tf = 3 > 4 #It has a calculated value
print(tf)
is_adult=age >= 18 #It has a calculated value
#provide three variables names for boolean values
is_child=age < 18 
is_senior=age >= 65

is_even=(age % 2) == 0
# "%" is the modulus operator, it gives the remainder of a division operation
# for example, 5 % 2 is 1, because 5 divided by 2 is 2 with a remainder of 1
print(is_even)

is_absent=True #It has a user provided value
is_child=False


#List logical operators
# and, or, not
#equal =
#smaller <
#greater >
#smaller or equal <=
#greater or equal >=
#equal ==
#not equal !=
#example
print("Is 3>2?",3 > 2) 
print("is 3<2?", 3 < 2) 

#Now lets work on if statements
#if (is a must)


if 3>4:   # : (colon is a must) (is like "then what?")
    print("Yes")
    print("Yes, that is true")
print("This is outside the if statement")

#What is a statement?
#A statement is a line of code that performs an action (instructions to the cpu)

print("We like colors")
color=input("Enter a color: ")
if color != "Blue":
    print("Wrong color")
else:
    print("Well done")