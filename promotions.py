from abc import ABC, abstractmethod
from validation import Validation

class Promotion(ABC):
    def __init__(self, name):
        try:
            Validation.validate_name(name)
            self.name = name
        except ValueError as e:
            print(e)



    @abstractmethod
    def apply_promotion(self,product, quantity):
        pass


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)


    def apply_promotion(self,product, quantity):
        discount = 0
        for i in range(2, quantity + 1):
            if i % 2 == 0:
                discount += product.price * 0.5
        return round(discount, 2)


class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)


    def apply_promotion(self, product, quantity):
        discount = 0
        for i in range(2, quantity + 1):
            if i % 3 == 0:
                discount += product.price
        return round(discount, 2)


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        Validation.is_valid_percentage(percent)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discount = 0
        for i in range(0, quantity):
            discount += (product.price * (self.percent / 100))
        return round(discount, 2)