import requests

_url_base = "https://api.bitfinex.com/v2/"


class Bitfinex(object):

    @classmethod
    def get_price(cls, order_currency, payment_currency='BTC'):
        """
        :param order_currency:
        :param payment_currency:
        :return: buy price, sell price
        """
        r = requests.get("{0}/ticker/{1}".format(_url_base, 't' + order_currency + payment_currency))
        return r.json()[0], r.json()[2]

    @classmethod
    def get_relative_price(cls, order_currency, payment_currency):
        """
        :param order_currency:
        :param payment_currency:
        :return: buy price, sell price
        """
        if payment_currency == 'BTC' or payment_currency == 'USD':
            return cls.get_price(order_currency, payment_currency)
        buy_order, sell_order = cls.get_price(order_currency)
        buy_payment, sell_payment = cls.get_price(payment_currency)
        return buy_order/sell_payment, sell_order/buy_payment


