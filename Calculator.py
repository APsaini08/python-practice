def calculator():
    print("Welcome to the Python CLI Calculator!")
    print("Type your expression using +, -, *, / (e.g., 12 + 5 * 3)")
    print("Type 'exit' to quit.\n")

    while True:
        expression = input(">>> ")

        if expression.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break

        try:
            # Evaluate the expression safely
            result = eval(expression)
            print("= ", result)
        except ZeroDivisionError:
            print("Error: Division by zero.")
        except SyntaxError:
            print("Error: Invalid syntax. Please enter a valid expression.")
        except Exception as e:
            print(f"Error: {str(e)}")

# Run the calculator
calculator()
