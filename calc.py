
class FormulaError(Exception):
    """Custom exception class for handling formula errors."""

    def __init__(self, message=""):
        self.message = f"{message}"

    def __str__(self):
        return self.message


def check_formula(formula):
    """Check the validity of the input formula."""
    if len(formula) != 3:
        raise FormulaError("Formula must be 3 elements.")
    try:
        first_num, operator, second_num = float(formula[0]), formula[1], float(formula[2])
    except ValueError:
        raise FormulaError("Values for num1 and num2 must be valid numbers")
    if operator not in ('+', '-', '*', '/', '%'):
        raise FormulaError(f'Invalid operator.Operator {operator} is unknown!!')
    return first_num, operator, second_num

def mini_calculator():
    """simulates a mini calculator, input formula and get the result."""
    print("Welcome to mini_calculator :)\n")
    while True:
        user_input = input("type formula or 'quit' to log out:\n >> ")
        if user_input.lower() == "quit":
            print("--" * 10 + " Good bye :)" + "--" * 10)
            break
        formula = user_input.split()
        print( formula)
        num1, operand, num2 = check_formula(formula)
        if operand == '+':
            result = num1 + num2
        elif operand =='-':
            result = num1 - num2
        elif operand == '*':
            result = num1 * num2
        else:   
            result = (num1 / num2) if operand == '/' else (num1 % num2)
        print(result)


if __name__ == "__main__":
    mini_calculator()
