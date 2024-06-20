# test_multiplication.py
import pytest
import time
import random
from calculator import Calculator, use_numpy

def test_long_running_one():
    # Simulating a long process
    print("Test 1 is running, simulating a long process...")
    time.sleep(4)  # Sleep for 120 seconds (2 minutes)
    assert True  # Simulating a successful test
    
def test_multiplication():
    calc = Calculator()
    result = calc.multiply(3, 4)
    time.sleep(16)  
    assert result == 12

def test_multiplicationFlaky():
    calc = Calculator()
    result = calc.multiply(2, 7)
    time.sleep(7)  

    # Introduce flakiness/random errors
    #if random.choice([True, False]):
    #   result += 1  # Intentionally wrong result half the time
    assert result == 14
