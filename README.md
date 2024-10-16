# mini-calculator
## Task:
* You're going to write an interactive calculator!
User input is assumed to be a formula that consist of a number,
an operator ( +, -, *, / and %), and another number, separated by white space (e.g. 1 + 1).
Split user input, and check whether the resulting list is valid:

- If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
- Try to convert the first and third input to a float (like so: float_value = float(str_value));
Catch any ValueError that occurs, and instead raise a FormulaError;
- If the second input is not '+','-',*,/, or % again raise a FormulaError;
- If the input is valid, perform the calculation and print out the result.
The user is then prompted to provide
new input, and so on, until the user enters quit.

## Excepted output:
  *  in>> 1 + 1
  * out<< 2.0
  *  in>> 3.2 - 1.5
  * out 1.7000000000000002
  * in>> quit
  * out<< quit the program!
