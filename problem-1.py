class Calculator:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def calculate(self, operation: str) -> float:
        if operation.lower() == "add" or operation == "+":
            return self.a + self.b
        elif operation.lower() == "subtract" or operation == "-":
            return self.a - self.b
        elif operation.lower() == "multiply" or operation == "*":
            return self.a * self.b
        elif operation.lower() == "divide" or operation == "/":
            if self.b == 0:
                return "Error: Cannot divide by zero."
            else:
                return self.a / self.b
        else:
            return "Invalid operation"

a_input = 10.5
b_input = 2.5
operation_input = "add"  

calc = Calculator(a_input, b_input)
result = calc.calculate(operation_input)
print("Result:", result)