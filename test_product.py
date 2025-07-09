import pytest
from products import Product


def test_product():
    assert Product("Iphone", 1500, 20)


def test_string_price():
    assert Product("Iphone", "", 20)


def test_string_quantity():
    assert Product("Iphone", 1500, "")


def test_empty_product():
    assert Product("", 1500, 20)


def test_negative_price():
    assert Product("Iphone", -1, 20)


def test_negative_product_quantity():
    assert Product("Iphone", 1500, -1)


def test_product_name_as_list():
    assert Product([], 1500, 20)


def test_product_price_as_list():
    assert Product("Ipad", [], 20)


def test_product_quantity_as_list():
    assert Product("Ipad", 1200, [])


def test_product_status_with_zero_quantity():
    desktop = Product("Desktop", 100, 1)
    desktop.buy(1)
    assert desktop.is_active() == False


def test_product_quantity_updates_and_get_return_output():
    laptop = Product("Laptop", 1000, 4)
    assert laptop.buy(2) == 2000
    assert laptop.get_quantity() == 2


def test_buying_larger_than_quantity():
    cd = Product("CD", 1000, 1)
    assert cd.buy(2) is None


print("All tests PASSED")
pytest.main()
