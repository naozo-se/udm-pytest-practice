import pytest

from src.bank_account import BankAccount
from unittest.mock import patch


def test_get_balance_in_currency():
    amount = BankAccount(1_000)  # US＄→日本￥
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"rate": 150}

        balance_JPY = amount.get_balance_in_currency("JPY")
        assert balance_JPY == 150_000, "変換後の値が正しくありません"
