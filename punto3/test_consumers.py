import numpy as np


from consumer_upper import check_bollinger, window_size, num_std_dev


def test_no_alert_triggered():
    # Set up test data
    price_window = [120, 140, 160, 180, 200]
    price = 190
    stock = "AAPL"

    # Call the function to be tested
    result = check_bollinger(price_window, price, stock)

    # Assert that no alert is returned
    assert result is None

if __name__ == '__main__':
    test_no_alert_triggered()