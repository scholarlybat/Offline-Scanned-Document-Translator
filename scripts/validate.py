# Build: 5a6768f9d6fc4bc63781d18ee1fd2159

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
