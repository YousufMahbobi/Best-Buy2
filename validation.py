class Validation:

    @staticmethod
    def validate_name(name:str):
        if not isinstance(name, str):
            raise TypeError('Product name must be a string')
        if not name:
            raise ValueError('Product name cannot be empty')


    @staticmethod
    def validate_price(price):
        if not isinstance(price, (float, int)):
            raise ValueError('Product price must be a float')

        if price < 0.0:
            raise ValueError('Product price cannot be negative or zero')


    @staticmethod
    def validate_quantity(quantity):
        if not isinstance(quantity, int):
            raise ValueError('Product quantity must be a int')

        if quantity < 0:
            raise ValueError('Product quantity cannot be negative or zero')


    @staticmethod
    def compare_quantities(quantity:int, requested_quantity:int, msg):
        if requested_quantity > quantity:
            if msg == "available_quantity_vs_requested_quantities":
                raise ValueError('Requested quantity cannot be greater than available quantity')
            else:
                raise ValueError('Requested quantity cannot greater than maximum quantity limit')


    @staticmethod
    def validate_user_menu_option(menu_option):
        if 0 < menu_option < 5:
            raise ValueError('Menu option must be between 1 and 4')

    @staticmethod
    def is_number(prompt):
            try:
                user_input = int(input(prompt))
                return user_input
            except ValueError:
                print('Error with your choice! Try again!')












