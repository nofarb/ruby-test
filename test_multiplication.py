# test_multiplication.py
import pytest
import time
import random
from calculator import Calculator

def test_long_running_one():
    # Simulating a long process
    print("Test 1 is running, simulating a long process...")
    time.sleep(20)  # Sleep for 120 seconds (2 minutes)
    assert True  # Simulating a successful test
    
def test_multiplication():
    calc = Calculator()
    result = calc.multiply(3, 4)
    # Introduce flakiness
    #  if random.choice([True, False]):
    #   result += 1  # Intentionally wrong result half the time
    assert result == 12

