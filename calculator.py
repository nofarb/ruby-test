
# calculator.py
import hashlib
import pickle
import numpy as np


class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, c):
        return a - c

    @staticmethod
    def multiply(a, e):
        return a * e

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
   
    @staticmethod
    def use_numpy():
        # This function uses numpy, which is not listed in requirements.txt
        return np.array([1, 2, 3]) * 2

    def insecure_hash(password: str) -> str:
        # MD5 is considered cryptographically broken and unsuitable for further use.
        return hashlib.md5(password.encode()).hexdigest()


    def insecure_deserialize(data: bytes):
        # Deserializing objects from untrusted sources with pickle is insecure.
        return pickle.loads(data)
    
    def read_any_file(file_path: str):
        # Insecure practice as it can lead to directory traversal attacks.
        with open(file_path, 'r') as file:
            return file.read()



# Placeholder for a sensitive data example (DO NOT USE IN PRODUCTION)
# API_KEY = "12345-abcde-67890-fghij"  # This should be removed and managed securely
