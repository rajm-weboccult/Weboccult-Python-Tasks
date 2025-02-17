class FormulaError(Exception):
    """Exception for invalid formulas."""
    pass

def calculate(formula):
    try:
        parts = formula.split()
        if len(parts) != 3: raise FormulaError("Input must consist of exactly three elements: number operator number")
        num1, operator, num2 = parts
        num1, num2 = float(num1), float(num2)
        if operator not in '+-': raise FormulaError("Operator must be '+' or '-'.")
        return num1 + num2 if operator == '+' else num1 - num2
    except (FormulaError, ValueError) as e:
        return f"Error: {e}"

def main():
    while (user_input := input("Enter a number with formula or type 'quit' to exit: ").strip()).lower() != "quit":
        print(calculate(user_input))
    print("Exiting the calculator. Thank you!")

if __name__ == "__main__":
    main()