class Product:
    def __init__(self, product_id, name, price, stock, transactions=None):
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)
        self.__stock = int(stock)
        self.__transactions = transactions if transactions is not None else []

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def get_transactions(self):
        return self.__transactions

    def update_stock(self, new_stock):
        if new_stock < 0:
            raise ValueError("Stock cannot be negative.")

        difference = new_stock - self.__stock

        self.__stock = new_stock

        transaction = {
            "type": "STOCK_UPDATE",
            "quantity": difference,
            "amount": abs(difference) * self.__price
        }

        self.__transactions.append(transaction)