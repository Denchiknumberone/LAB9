
import pytest

# Тесты доставки по городу
@pytest.mark.parametrize("price,expected", [
    (0, "500"),
    (5000, "500"),
    (9999, "500"),
    (10000, "0"),
    (15000, "0"),
    (10001, "0")
])
def test_city_delivery(page, price, expected):
    page.goto("http://127.0.0.1:8000/delivery.html")

    page.select_option("#type", "city")
    page.fill("#price", str(price))
    page.click("#calculateBtn")

    assert page.text_content("#result") == expected


# Тесты доставки по области
@pytest.mark.parametrize("price,expected", [
    (0, "1000"),
    (5000, "1000"),
    (9999, "1000"),
    (10000, "0"),
    (15000, "0"),
    (10001, "0")
])
def test_region_delivery(page, price, expected):
    page.goto("http://127.0.0.1:8000/delivery.html")

    page.select_option("#type", "region")
    page.fill("#price", str(price))
    page.click("#calculateBtn")

    assert page.text_content("#result") == expected
