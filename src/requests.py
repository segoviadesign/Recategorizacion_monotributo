"""Minimal requests stub used for local testing without external dependency."""
from typing import Any, Dict


class Response:
    def __init__(self, data: Dict[str, Any], status_code: int = 200):
        self._data = data
        self.status_code = status_code

    def raise_for_status(self) -> None:
        if not (200 <= self.status_code < 300):
            raise Exception(f"HTTP {self.status_code}")

    def json(self) -> Dict[str, Any]:
        return self._data

def get(url: str, params: Dict[str, Any] | None = None, cert: tuple | None = None) -> Response:
    # In a real implementation this would perform an HTTP request.
    # Here it returns an empty response as placeholder.
    return Response({"invoices": []})
