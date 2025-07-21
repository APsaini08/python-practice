def convert_temperature(value, from_unit, to_unit):
    """Converts temperature from one unit to another."""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    # Convert input to Celsius as a base
    if from_unit == 'c':
        celsius = value
    elif from_unit == 'f':
        celsius = (value - 32) / 1.8
    elif from_unit == 'k':
        celsius = value - 273.15
    else:
        raise ValueError("Invalid source unit")

    # Convert from Celsius to target unit
    if to_unit == 'c':
        return celsius
    elif to_unit == 'f':
        return celsius * 9/5 + 32
    elif to_unit == 'k':
        return celsius + 273.15
    else:
        raise ValueError("Invalid target unit")


def convert_to_all(value, unit):
    """Converts the given temperature to all 3 units (C, F, K)."""
    c = convert_temperature(value, unit, 'c')
    f = convert_temperature(value, unit, 'f')
    k = convert_temperature(value, unit, 'k')
    return c, f, k


def main():
    print("Welcome to the Temperature Converter!")
    print("Format: Enter temperature with unit (e.g., 25C, -40F, 300K)")
    print("Type 'exit' anytime to quit.\n")

    while True:
        temp = input("Enter the temperature (with unit): ").strip().lower()

        if temp == 'exit':
            print("Goodbye!")
            break

        # Validation
        if len(temp) < 2 or temp[-1] not in ('c', 'f', 'k'):
            print("Error: Invalid input format. Example: 25C, 100F, 300K")
            continue

        # Extract value and unit
        try:
            value = float(temp[:-1])
        except ValueError:
            print("Error: Invalid numeric value")
            continue

        unit = temp[-1]

        # Convert to all units
        try:
            c, f, k = convert_to_all(value, unit)
            print(f"\nConverted Values:")
            print(f"{c:.2f} °C")
            print(f"{f:.2f} °F")
            print(f"{k:.2f} K\n")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
