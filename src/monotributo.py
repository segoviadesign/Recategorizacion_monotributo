from typing import Dict

# Sample category thresholds, values are annual gross income limits
CATEGORY_LIMITS: Dict[str, float] = {
    "A": 8992597.87,
    "B": 13175201.52,
    "C": 18473166.15,
    "D": 22934610.05,
    "E": 26977793.60,
    "F": 33809379.57,
    "G": 40431835.35,
    "H": 61344853.64,
    "I": 68664410.05,
    "J": 78632948.76,
    "K": 94805682.90,
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
