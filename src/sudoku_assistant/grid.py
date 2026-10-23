def box_start(index: int) -> int:
    """Return the first row or column of the 3x3 box that contains the given index."""
    return (index // 3) * 3
