from src.monotributo import get_category_for_sales, needs_recategorization


def test_category_for_sales():
    assert get_category_for_sales(200000) == "A"
    assert get_category_for_sales(500000) == "D"


def test_needs_recategorization():
    assert not needs_recategorization("D", 600000)
    assert needs_recategorization("D", 700000)
