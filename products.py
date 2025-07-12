import validation
from validation import Validation
from promotions import *

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
            self._promotion: None
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
        if self._promotion:
            print(f'{self.name},'
                  f' Price: {self.price},'
                  f' Quantity: {self.quantity},'
                  f' promotion:{self._promotion.name}'
                 )
        else:
            print(f'{self.name},'
                  f' Price: {self.price},'
                  f' Quantity: {self.quantity},'
                 )


    def buy(self, quantity):
        try:
            __promotion = 0
            Validation.validate_quantity(quantity)
            if self.is_active():
                if type(self) == LimitedProduct:
                    Validation.compare_quantities(self.maximum,
                                                  quantity,
                                                  "maximum_quantity_limit_vs_requested_quantities"
                                                  )

                if type(self._promotion) == ThirdOneFree:
                    for i in range(2, quantity + 1):
                        if i % 2 == 0:
                            quantity += 1

                if type(self) == Product or type(self) == LimitedProduct:
                    Validation.compare_quantities(self.quantity,
                                                  quantity,
                                             "available_quantity_vs_requested_quantities"
                                                 )

                    self.quantity = self.get_quantity() - quantity
                    self.check_and_deactivate_product_out_of_stock()
                if self._promotion:
                    __promotion += self._promotion.apply_promotion(self, quantity)

                return (quantity * self.price) - __promotion
            return 0
        except Exception as e:
            return 0

    def check_and_deactivate_product_out_of_stock(self):
        if self.quantity == 0:
            self.deactivate()

    def set_promotion(self, promotion):
        if not isinstance(promotion, Promotion):
            raise TypeError("Expected a Promotion instance")
        self._promotion = promotion

    def get_promotion(self):
        return self._promotion


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)

    def set_quantity(self, quantity):
        self.quantity = 0

    def show(self):
        if self._promotion:
            print(f'{self.name}, '
                  f'Price: {self.price}'
                  f'Promotion: {self._promotion.name}'
                  )
        else:
            print(f'{self.name}, '
                  f'Price: {self.price}'
                 )



class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        try:
            Validation.validate_quantity(maximum)
            super().__init__(name, price, quantity)
            self.maximum = maximum
        except Exception as e:
            print(e)

    def show(self):
        if self._promotion:
            print(f'{self.name}, Price: '
                  f'{self.price} Quantity: '
                  f'{self.quantity} Max Quantity: '
                  f'{self.maximum}'
                  f'Promotion: {self._promotion.name}'
                 )
        else:
            print(f'{self.name}, Price: '
                  f'{self.price} Quantity: '
                  f'{self.quantity} Max Quantity: '
                  f'{self.maximum}'
                  )












