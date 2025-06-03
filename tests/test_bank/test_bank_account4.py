import pytest

from src.bank_account import BankAccount


@pytest.mark.parametrize(
    "initial_amount, deposit_amount, excepted_balance",
    [(0, 1000, 1000), (1000, 1500, 2500), (999_999, 1, 1_000_000)],
)
def test_bank_account_initial_balance(initial_amount, deposit_amount, excepted_balance):
    amount = BankAccount(initial_amount)
    assert amount.deposit(deposit_amount) == excepted_balance, "残高計算が正しくありません"
