# Build: 2c4446a90deecc116ae1f1e570ceb6e5

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
