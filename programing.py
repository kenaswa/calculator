#print("Hello, World")

firstName=input("Enter Your File Name: ")#"Kennedy"
lastName="Aswa"
age=40
print(f"My Name is {firstName} {lastName} {firstName[4::-3]} and am {age} years old.")

num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == '+':
    print(f"Result: {num1 + num2}")
elif operator == '-':
    print(f"Result: {num1 - num2}")
elif operator == '*':
    print(f"Result: {num1 * num2}")
elif operator == '/':
    print(f"Result: {num1 / num2}")
else:
    print("Invalid operator")
    print("End Code")