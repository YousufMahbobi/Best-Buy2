import products
import store
from validation import Validation
import promotions

product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250),
                 products.NonStockedProduct("Windows License", price=125),
                 products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]
best_buy = store.Store(product_list)

second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)


product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)




def start(store):

    while True:
        display_menu()
        user_menu_option = get_user_menu_option()
        process_menu_choice(user_menu_option, store)


def display_all_products(store):
    product_list = store.get_all_products()
    print("\n------")
    for row_number, product in enumerate(product_list, start=1):
        print(f'{row_number}. {product.name}, '
              f'Price: {product.price},'
              f' Quantity: {product.quantity}'
              )
    print("------")

def display_menu():
    print("\nStore Menu")
    print("-------------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def get_user_menu_option():
    return Validation.is_number("Enter your choice: ")


def make_order(store):
    shopping_list = []
    total_order_price = 0

    display_all_products(store)

    print("When you want to finish order, enter empty text.")

    while True:
        product_number = input("Which product # do you want? ")
        product_amount = input("What amount do you want? ")

        if product_number.strip() == "" and product_amount.strip() == "":
            break
        else:
            try:
                product_number = int(product_number) - 1
            except ValueError:
                product_number = -1

            try:
                product_amount = int(product_amount)
            except ValueError:
                product_amount = 0

            if 0 <= product_number < len(product_list) and product_amount > 0:
                product = product_list[product_number]
                if product.quantity >= product_amount:
                    shopping_list.append((product, product_amount))
                    total_order_price = store.order(shopping_list)
                    if total_order_price == 0:
                        print("Error adding product!\n")
                    else:
                        print("Product added to list!\n")
                else:
                    print("Error adding product!\n")
            else:
                print("Error adding product!\n")

    print("********")
    if total_order_price != 0:
        print(f"Order made! Total payment: ${total_order_price}")
    else:
        print(f"No Order made!")


def process_menu_choice(user_menu_option, store):
    if user_menu_option == 1:
        display_all_products(store)
    elif user_menu_option == 2:
        total_products_quantity_in_store = store.get_total_quantity()
        print(f'Total of {total_products_quantity_in_store} items in store')
    elif user_menu_option == 3:
        make_order(store)
    elif user_menu_option == 4:
        exit()
    else:
        start(best_buy)


if __name__ == "__main__":
    start(best_buy)