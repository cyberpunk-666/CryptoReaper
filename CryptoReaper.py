import krakenex
from pykrakenapi import KrakenAPI
import time

# Configurer le client Kraken avec vos clés API
api_key = 'YB4yEgwRW8RJTAl+NKRIluvF4Gh7wCP/OjQDpbM/BEL/klKGK5TDNSBh'
api_secret = 'uy+9+cTzwtAHL0k9T2Ez9ymx/Fr+O8FZ7cgpZ6g8LjlWDf5cZICCWvkGahbZHy9zQFeEFK5Vw5K+9BzqLtP++Q=='

api = krakenex.API(api_key, api_secret)
kraken = KrakenAPI(api)

def get_balance(currency):
    balance = kraken.get_account_balance()
    return balance[currency]

def place_order(pair, type, ordertype, volume, price=None):
    if price:
        response = kraken.add_standard_order(pair=pair, type=type, ordertype=ordertype, volume=volume, price=price)
    else:
        response = kraken.add_standard_order(pair=pair, type=type, ordertype=ordertype, volume=volume)
    return response

def check_order_status(txid):
    response = kraken.query_orders_info(txid)
    return response

def main():
    pair = 'XBTEUR'
    buy_price_threshold = 25000  # Exemple de prix d'achat
    sell_price_threshold = 30000  # Exemple de prix de vente
    volume = 0.001  # Volume de BTC à acheter/vendre

    while True:
        ticker = kraken.get_ticker_information(pair)
        current_price = float(ticker['b'][0][0])  # Prix actuel de l'offre
        print(f"current_price:{current_price}")

        if current_price < buy_price_threshold:
            print(f"Achat de {volume} BTC à {current_price} EUR")
            place_order(pair, 'buy', 'limit', volume, current_price)

        elif current_price > sell_price_threshold:
            print(f"Vente de {volume} BTC à {current_price} EUR")
            place_order(pair, 'sell', 'limit', volume, current_price)

        time.sleep(1)  # Attendre une minute avant de vérifier à nouveau

if __name__ == "__main__":
    main()
