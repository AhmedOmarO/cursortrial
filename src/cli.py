"""
Command-line interface for the calculator application.
"""
from typing import Optional
from calculator import Calculator


def get_number_input(prompt: str) -> Optional[float]:
    """Get numerical input from the user."""
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


def main():
    """Main CLI function."""
    calculator = Calculator()
    operations = {
        '1': ('Add', calculator.add),
        '2': ('Subtract', calculator.subtract),
        '3': ('Multiply', calculator.multiply),
        '4': ('Divide', calculator.divide),
    }

    while True:
        print("\nCalculator Menu:")
        print("---------------")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("5. Exit")

        choice = input("\nSelect operation (1-5): ")

        if choice == '5':
            print("Goodbye!")
            break

        if choice not in operations:
            print("Invalid choice. Please select 1-5.")
            continue

        x = get_number_input("Enter first number: ")
        if x is None:
            continue

        y = get_number_input("Enter second number: ")
        if y is None:
            continue

        operation_name, operation_func = operations[choice]
        try:
            result = operation_func(x, y)
            print(f"\nResult of {operation_name.lower()}: {result}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main() 