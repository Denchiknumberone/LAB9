import pytest

# Тесты для города (city) — базовые, бесплатные и граничные
@pytest.mark.parametrize("price,expected", [
    (0, "500"), (5000, "500"), (9999, "500"), 
    (10000, "0"), (15000, "0"), (10001, "0")
])
def test_city_delivery(page, price, expected):
    page.fill("#price", str(price))
    page.click("#calculateBtn")
    assert page.text_content("#result") == expected

# Тесты для области (region) — базовые, бесплатные и граничные
@pytest.mark.parametrize("price,expected", [
    (0, "1000"), (5000, "1000"), (9999, "1000"), 
    (10000, "0"), (15000, "0"), (10001, "0")
])
def test_region_delivery(page, price, expected):
    page.select_option("#type", "region")
    page.fill("#price", str(price))
    page.click("#calculateBtn")
    assert page.text_content("#result") == expected
