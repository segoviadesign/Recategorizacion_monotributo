from typing import Dict

# Sample category thresholds, values are annual gross income limits
CATEGORY_LIMITS: Dict[str, float] = {
    "A": 208739.25,
    "B": 313108.87,
    "C": 417478.51,
    "D": 626217.78,
    "E": 834957.03,
    "F": 1043696.27,
    "G": 1252435.53,
    "H": 2087399.51,
    "I": 2311312.05,
    "J": 2523864.90,
    "K": 2826214.67,
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
