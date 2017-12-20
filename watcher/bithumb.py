"""

"""
import requests

_public_url_base = "https://api.bithumb.com/public"


class Bithumb(object):

    @classmethod
    def get_relative_price(cls, order_currency, payment_currency):
        buy_order, sell_order = cls.get_price(order_currency)
        buy_payment, sell_payment = cls.get_price(payment_currency)
        return buy_order / sell_payment, sell_order / buy_payment

    @classmethod
    def get_price(cls, symbol):
        r = requests.get("{0}/ticker/{1}".format(_public_url_base, symbol))
        assert (r.status_code == 200)
        data = r.json()['data']
        return float(data["buy_price"]), float(data["sell_price"])
