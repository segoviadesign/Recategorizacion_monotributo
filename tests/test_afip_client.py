from datetime import datetime
from unittest.mock import patch

from src.afip_client import AFIPClient, sum_invoices_total, requests



def mock_get(*args, **kwargs):
    class MockResponse:
        def __init__(self):
            self.status_code = 200

        def raise_for_status(self):
            pass

        def json(self):
            return {
                "invoices": [
                    {"total": 100.0},
                    {"total": 50.0},
                ]
            }

    return MockResponse()


def test_get_invoices_and_sum():
    client = AFIPClient()
    start = datetime(2024, 7, 1)
    end = datetime(2025, 6, 30)
    with patch.object(requests, "get", side_effect=mock_get):
        invoices = client.get_invoices(start, end)
    assert len(invoices) == 2
    assert sum_invoices_total(invoices) == 150.0
