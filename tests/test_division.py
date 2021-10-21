import pytest
from src.calculator import Calculator

@pytest.fixture
def calculator() -> Calculator:
    return Calculator()

def test_division(calculator):
    assert calculator.division(4, 2) == 2
    