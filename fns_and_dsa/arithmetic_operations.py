def perform_operation(num1, num2, operation): 
    if num2 == 0 and operation == "divide":
        return f"Cannot {operation} {num1} with {num2}"
    else: 
        match operation:
            case "add":
                result = num1 + num2
                return result
            case "subtract":
                result = num1 - num2
                return result
            case "multiply":
                result = num1 * num2
                return result
            case "divide":
                result = num1 / num2
                return result
            case _ :
                return f"Invalid operation option '{operation}'"
