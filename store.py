from validation import Validation

class Store:
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.products:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self):
        return [product for product in self.products if product.active]

    def order(self, shopping_list):
        total_price = 0
        if shopping_list:
            for shopping_item in shopping_list:
                order_product, order_quantity = shopping_item
                total_price += order_product.buy(order_quantity)
        return total_price

















