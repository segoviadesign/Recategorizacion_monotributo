import os
from datetime import datetime
from typing import List, Dict, Any

from . import requests


class AFIPClient:
    """Simple client to fetch electronic invoices from AFIP."""

    def __init__(self) -> None:
        self.cuit = os.getenv("AFIP_CUIT", "")
        self.cert_path = os.getenv("AFIP_CERT_PATH", "")
        self.key_path = os.getenv("AFIP_KEY_PATH", "")
        self.base_url = os.getenv("AFIP_WS_URL", "https://dummy.afip/wsfe")

    def get_invoices(self, start: datetime, end: datetime) -> List[Dict[str, Any]]:
        params = {
            "cuit": self.cuit,
            "start": start.strftime("%Y-%m-%d"),
            "end": end.strftime("%Y-%m-%d"),
        }
        response = requests.get(
            self.base_url,
            params=params,
            cert=(self.cert_path, self.key_path) if self.cert_path and self.key_path else None,
        )
        response.raise_for_status()
        data = response.json()
        return data.get("invoices", [])


def sum_invoices_total(invoices: List[Dict[str, Any]]) -> float:
    """Sum the total amount of all invoices returned by :meth:`get_invoices`."""
    total = 0.0
    for inv in invoices:
        total += float(inv.get("total", 0))
    return total


def get_total_facturado(fecha_desde: str, fecha_hasta: str) -> float:
    """Helper used by the web app to sum invoices in a date range."""
    client = AFIPClient()
    start = datetime.strptime(fecha_desde, "%Y%m%d")
    end = datetime.strptime(fecha_hasta, "%Y%m%d")
    invoices = client.get_invoices(start, end)
    return sum_invoices_total(invoices)
