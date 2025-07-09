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
            print(e)


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
                Validation.validate_quantity_available(self.quantity, quantity)
                self.quantity = self.get_quantity() - quantity
                self.check_and_deactivate_product_out_of_stock()
                return quantity * self.price
            return 0
        except Exception as e:
            print(e)

    def check_and_deactivate_product_out_of_stock(self):
        if self.quantity == 0:
            self.deactivate()

