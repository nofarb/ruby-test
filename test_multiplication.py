# test_multiplication.py
import pytest
import random
from calculator import Calculator

def test_multiplication():
    calc = Calculator()
    result = calc.multiply(3, 4)
    # Introduce flakiness
    if random.choice([True, False]):
        result += 1  # Intentionally wrong result half the time
    assert result == 12
