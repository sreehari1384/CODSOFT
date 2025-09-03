def is_number(value):
    return value.replace('.', '', 1).isdigit() or (value.startswith('-') and value[1:].replace('.', '', 1).isdigit())

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    elif operation == '%':
        if num2 == 0:
            return "Error: Modulus by zero"
        return num1 % num2
    elif operation == '**':
        return num1 ** num2
    elif operation == '//':
        if num2 == 0:
            return "Error: Floor division by zero"
        return num1 // num2
    else:
        return "Invalid operation"

def main():
    print("==== Universal Calculator ====")
    print("Available operations: +, -, *, /, %, **, //")

    num1_input = input("Enter first number: ")
    num2_input = input("Enter second number: ")
    operation = input("Enter an operation (+, -, *, /, %, **, //): ").strip()
    if not is_number(num1_input) or not is_number(num2_input):
        print("Error: Invalid number input.")
        return

    num1 = float(num1_input)
    num2 = float(num2_input)

    result = calculate(num1, num2, operation)
    print(f"Result: {num1} {operation} {num2} = {result}")

main()
