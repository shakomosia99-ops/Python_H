import pytest


def process_orders(orders, inventory):

    successful_orders = []

    for order in orders:
        product = order["product"]
        quantity = order["quantity"]

        if product not in inventory:
            raise ValueError(f"Product '{product}' not found in inventory")

        if quantity > inventory[product]:
            raise ValueError(f"Not enough stock for '{product}'")

        inventory[product] -= quantity
        successful_orders.append(order)

    return successful_orders


def test_product_not_in_inventory():
    orders = [{"product": "banana", "quantity": 3}]
    inventory = {"apple": 10}

    with pytest.raises(ValueError, match="Product 'banana' not found in inventory"):
        process_orders(orders, inventory)


def test_not_enough_stock():
    orders = [{"product": "apple", "quantity": 15}]
    inventory = {"apple": 10}

    with pytest.raises(ValueError, match="Not enough stock for 'apple'"):
        process_orders(orders, inventory)


def test_successful_order_deducts_inventory():
    orders = [
        {"product": "apple", "quantity": 5},
        {"product": "banana", "quantity": 2},
    ]
    inventory = {"apple": 10, "banana": 5}

    result = process_orders(orders, inventory)

    assert result == orders
    assert inventory["apple"] == 5
    assert inventory["banana"] == 3


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
