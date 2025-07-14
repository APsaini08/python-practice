value = input("Enter the value: ").replace(" ", "")  # Remove spaces
x = 0
leng = len(value)

if leng == 0:
    print("Error: Empty input")
    exit()

# Check if it starts with an operator
if value[0] in ('-', '+', '*', '/'):
    print("Error: Expression can't start with operator")
    exit()

# Check if it ends with an operator
if value[-1] in ('-', '+', '*', '/'):
    print("Error: Expression can't end with operator")
    exit()

result = int(value[0])
x = 1

while x < leng:
    operator = value[x]

    if x+1 >= leng:
        print("Error: Operator at end without number")
        break

    next_char = value[x + 1]

    if not next_char.isdigit():
        print("Error: Invalid number after operator")
        break

    number = int(next_char)

    if operator == '+':
        result += number
    elif operator == '-':
        result -= number
    elif operator == '*':
        result *= number
    elif operator == '/':
        if number == 0:
            print("Error: Division by zero")
            break
        result /= number
    else:
        print(f"Error: Unknown operator '{operator}'")
        break

    x += 2

print("Result:", result)
