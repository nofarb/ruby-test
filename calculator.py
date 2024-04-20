
# calculator.py

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, c):
        return a - c

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b


# Placeholder for a sensitive data example (DO NOT USE IN PRODUCTION)
# API_KEY = "12345-abcde-67890-fghij"  # This should be removed and managed securely
