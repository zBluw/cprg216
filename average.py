print("Welcome to the average calculation program")

while True:
    print("Please enter 3 numbers")
    a=float(input(""))
    b=float(input(""))
    c=float(input(""))

    sum= a+b+c
    average = sum/3

    print("The average is", average)
    print("Do you want to continue? Yes/No")

    Answer = input("").strip().lower()
    if Answer == "no":
        break
print("Done")

