from typing import Dict

# Sample category thresholds, values are annual gross income limits
# Simplified annual sales limits used for testing purposes
CATEGORY_LIMITS: Dict[str, float] = {
    "A": 250_000.0,
    "B": 350_000.0,
    "C": 450_000.0,
    "D": 600_000.0,
}


def get_category_for_sales(total_sales: float) -> str:
    """Return the category that fits the given total sales."""
    for category, limit in CATEGORY_LIMITS.items():
        if total_sales <= limit:
            return category
    return "K"


def needs_recategorization(current_category: str, total_sales: float) -> bool:
    """Return True if sales exceed current category limit."""
    limit = CATEGORY_LIMITS.get(current_category.upper())
    if limit is None:
        raise ValueError("Unknown category: %s" % current_category)
    return total_sales > limit


def determinar_categoria(total_facturado):
    categorias = [
        {"categoria": "A", "max_facturacion": 2_108_288.01},
        {"categoria": "B", "max_facturacion": 3_133_941.63},
        {"categoria": "C", "max_facturacion": 4_387_518.23},
        {"categoria": "D", "max_facturacion": 5_449_094.55},
        {"categoria": "E", "max_facturacion": 6_416_528.72},
        {"categoria": "F", "max_facturacion": 8_020_661.11},
        {"categoria": "G", "max_facturacion": 9_624_793.52},
        {"categoria": "H", "max_facturacion": 11_916_410.77},
        {"categoria": "I", "max_facturacion": 13_337_213.22},
        {"categoria": "J", "max_facturacion": 15_285_088.45},
        {"categoria": "K", "max_facturacion": 16_957_968.71},
    ]
    
    for cat in categorias:
        if total_facturado <= cat["max_facturacion"]:
            return cat["categoria"]
    
    return "Fuera de Monotributo"