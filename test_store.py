from Store import product_details

def test_product_details():
    result = product_details(1, "Laptop", 5, 119990.00)
    expected_result = ("Product ID: 1\n"
                      "Name: Laptop\n"
                      "Quantity: 5\n"
                      "Price: ₹119990.00")

    assert result == expected_result