class Product:
    def __init__(self, product_id, name, price, stock, transactions=None):
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)
        self.__stock = int(stock)
        self.__transactions = transactions if transactions is not None else []

    