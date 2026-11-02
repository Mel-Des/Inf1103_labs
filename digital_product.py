class DigitalProduct(Product):

    def __init__(self, product_id, name, price, stock, download_size, transactions=None):
        super().__init__(product_id, name, price, stock, transactions)
        self.__download_size = float(download_size)

        if self.__download_size < 0:
            raise ValueError("Download size cannot be negative.")

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size:.2f} MB")

    def get_fulfilment_info(self):
        return "Delivered digitally."

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data