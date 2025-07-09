import validation
from validation import Validation

class Product:
    def __init__(self, name, price, quantity):
        try:
            Validation.validate_name(name)
            Validation.validate_price(price)
            Validation.validate_quantity(quantity)

            self.name = name
            self.price = price
            self.quantity = quantity
            self.active = True
        except Exception as e:
            print(e)


    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        try:
            Validation.validate_quantity(quantity)
            self.quantity = quantity + self.get_quantity()
            self.check_and_deactivate_product_out_of_stock()
        except Exception as e:
            return e


    def is_active(self):
        return self.active


    def deactivate(self):
        self.active = False

    def show(self):
        print(f'{self.name}, Price: {self.price}, Quantity: {self.quantity}')

    def buy(self, quantity):
        try:
            Validation.validate_quantity(quantity)
            if self.is_active():
                if type(self) == Product:
                    Validation.compare_quantities(self.quantity,
                                                           quantity,
                                                           "available_quantity_vs_requested_quantities"
                                                          )
                    self.quantity = self.get_quantity() - quantity
                    self.check_and_deactivate_product_out_of_stock()

                return quantity * self.price
            return 0
        except Exception as e:
            return e

    def check_and_deactivate_product_out_of_stock(self):
        if self.quantity == 0:
            self.deactivate()


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)

    def set_quantity(self, quantity):
        self.quantity = 0

    def show(self):
        print(f'{self.name}, Price: {self.price}')


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        try:
            Validation.validate_quantity(maximum)
            super().__init__(name, price, quantity)
            self.maximum = maximum
        except Exception as e:
            print(e)

    def show(self):
        print(f'{self.name}, Price: '
              f'{self.price} Quantity: '
              f'{self.quantity} Max Quantity: '
              f'{self.maximum}'
             )

    def buy(self, quantity):
        try:
            Validation.validate_quantity(quantity)
            if self.is_active():
                Validation.compare_quantities(self.maximum,
                                              quantity,
                                              "requested_quantity_vs_max_quantity"
                                             )
                Validation.compare_quantities(self.quantity,
                                              quantity,
                                              "available_quantity_vs_requested_quantities"
                                             )
                self.quantity = self.get_quantity() - quantity
                self.check_and_deactivate_product_out_of_stock()
                return quantity * self.price
            return 0
        except Exception as e:
            return e









