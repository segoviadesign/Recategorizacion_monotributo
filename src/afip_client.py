import os
from datetime import datetime
from typing import List, Dict
from . import requests


class AFIPClient:
    """Simple client for AFIP WSFE."""

    def __init__(self) -> None:
        self.cuit = os.getenv("AFIP_CUIT")
        self.cert_path = os.getenv("AFIP_CERT_PATH")
        self.key_path = os.getenv("AFIP_KEY_PATH")
        self.base_url = os.getenv("AFIP_WS_URL", "https://dummy.afip/wsfe")

    def get_invoices(self, start_date: datetime, end_date: datetime) -> List[Dict]:
        """Return invoices issued between two dates."""
        params = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "cuit": self.cuit,
        }
        response = requests.get(
            self.base_url,
            params=params,
            cert=(self.cert_path, self.key_path),
        )
        response.raise_for_status()
        data = response.json()
        return data.get("invoices", [])


def sum_invoices_total(invoices: List[Dict]) -> float:
    """Sum total amount from invoice list."""
    return sum(float(inv.get("total", 0)) for inv in invoices)
