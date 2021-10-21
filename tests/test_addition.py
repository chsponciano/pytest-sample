import pytest
from src.calculator import Calculator

@pytest.fixture
def calculator() -> Calculator:
    return Calculator()

def test_addition(calculator):
    assert calculator.addition(2, 2) == 4
    