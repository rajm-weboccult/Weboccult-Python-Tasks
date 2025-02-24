class FormulaError(Exception):
    """Exception for invalid formulas."""
    pass

def calculate(formula):
    try:
        parts = formula.split()
        if len(parts) != 3:
            raise FormulaError("Input must consist of exactly three elements: number <space> operator <space> number 🧮. Example: '5 + 3'")
        num1, operator, num2 = parts
        
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            raise FormulaError("Both inputs must be valid numbers. 🔢")
        
        if operator not in '+-':
            raise FormulaError("Operator must be '+' or '-' ")
        
        return num1 + num2 if operator == '+' else num1 - num2
    
    except FormulaError as e:
        return f"Error ❌: {e}"

def main():
    print("\nWelcome to the Simple Calculator! 🧮")
    print("You can perform addition (+) or subtraction (-).")
    print("Format: <number> <space> <operator> <space> <number>")
    print("Example: '5 + 3' or '10 - 4'")
    print("Type 'quit' to exit the calculator. 👋\n")
    
    while (user_input := input("Enter a formula (e.g., '5 + 3') or type 'quit' to exit: ").strip()).lower() != "quit":
        result = calculate(user_input)
        if isinstance(result, float): 
            print(f"Result: {result} ")
        else:
            print(result) 
    
    print("\nExiting the calculator. Thank you for using it! 👋😊")

if __name__ == "__main__":
    main()