num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /) ")

if num2 == 0 and operation == "/":
    print(f"Cannot divide by zero")

else:
    match operation:
        case "+":
            answer = num1 + num2
            print(f"The result is {answer}.")
            
        case "-":
            answer = num1 - num2
            print(f"The result is {answer}.")
        
        case "*":
            answer = num1 * num2
            print(f"The result is {answer}.")
            
        case "/":
            answer = num1 / num2
            print(f"The result is {answer}.")  
        case _:
            print("Error cannot calculate")
        
