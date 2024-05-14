from datetime import datetime
from decimal import Decimal

from pycbrf import ExchangeRates


def get_currency_rates(currency: str) -> Decimal:
    """Получает курс валюты."""
    current_date = datetime.now().strftime("%Y-%m-%d")
    rates = ExchangeRates(current_date)
    currency = check_currency(currency)
    filtered_rates = list(filter(lambda x: x.code == currency, rates.rates))
    if filtered_rates:
        currency_rates = filtered_rates[0].rate
        return Decimal(currency_rates)
    return Decimal(0)


def check_currency(currency: str) -> str:
    """Изменяет код валюты 'BYR' на 'BYN'."""
    if currency == "BYR":
        return "BYN"
    return currency
