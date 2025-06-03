import pytest
import requests

from src.bank_account import BankAccount

@pytest.fixture
def initial_amount():
    return BankAccount(1000)
