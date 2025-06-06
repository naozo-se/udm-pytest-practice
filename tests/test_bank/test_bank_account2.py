import pytest

from src.bank_account import BankAccount


# @pytest.fixture
# def initial_amount():
#     return BankAccount(1000)


def test_bank_account_initial_balance(initial_amount):
    assert initial_amount.get_balance() == 1000, "残高が正しくありません"


def test_withdraw_sufficient_balance(initial_amount):
    initial_amount.withdraw(500)
    assert initial_amount.get_balance() == 500, "引き出し後の残高が間違っています"


def test_withdraw_negative_amount(initial_amount):
    with pytest.raises(ValueError, match="引き出し額は正の値でなければなりません"):
        initial_amount.withdraw(-100)
