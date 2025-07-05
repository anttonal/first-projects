"""
COMP.CS.100 - round 10.
Student: Antton Alivuotila
Email: antton.alivuotila@tuni.fi
Student number: 151259218

Assignment: Tuote
"""


class Product:
    """
    This class defines a simplified product for sale in a store.
    """
    def __init__(self, name, price):
        """
        gives the product a name and a price
        :param name: str, the name of the product
        :param price: float, the price of the product
        """
        self.__name = name
        self.__price = price
        self.__sale = 0

    def set_sale_percentage(self, sale):
        """
        sets sale number
        :param sale: int, percentage of sale
        """
        self.__sale = sale

    def get_price(self):
        """
        calculates the price of a product
        :return: float, returns the price
        """
        return self.__price*(1-(self.__sale/100))

    def printout(self):
        """
        prints out the pricing and sale of a product
        """
        print(self.__name)
        print(f"  price: {self.__price:.2f}")
        print(f"  sale%: {self.__sale:.2f}")


def main():

    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
