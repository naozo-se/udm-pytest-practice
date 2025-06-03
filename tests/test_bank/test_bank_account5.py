import pytest
from src.bank_account import BankAccount

@pytest.mark.raises
def test_withdraw_insufficient_balance():
    amount = BankAccount(500)
    with pytest.raises(ValueError, match="残高不足です"):
        amount.withdraw(1000)


# スキップ設定
@pytest.mark.skip
def test_withdraw_insufficient_balance2():
    amount = BankAccount(500)
    with pytest.raises(ValueError, match="残高不足です"):
        amount.withdraw(1000)

