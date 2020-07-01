print("hello world")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

#first task
if (num1 > num2 or num2 > num3):
    print("Input is invalid")
else:
    if (num1 == num2 and num2 == num3):
        print("this is equilateral")
    elif(num1 == num2 or num2 == num3 or num1 == num3):
        print("this is isosceles")
    else:
        print("this is scalene")
