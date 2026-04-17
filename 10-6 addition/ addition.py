print("Enter two numbers to add them together.")

try:
    num1 = input("First number: ")
    num2 = input("Second number: ")
    
    num1 = int(num1)
    num2 = int(num2)
    
    result = num1 + num2
    
    print(f"The result is: {result}")

except ValueError:
    print("Oops! Please enter valid numbers only.")
