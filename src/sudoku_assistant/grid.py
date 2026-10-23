import numpy as np


def box_start(index: int) -> int:
    """Return the first row or column of the 3x3 box that contains the given index."""
    return (index // 3) * 3


def is_valid_placement(grid: np.ndarray, row: int, col: int, digit: int) -> bool:
    """Check if placing the digit at the given row and column is valid."""
    if digit in grid[row, :]:
        return False
    if digit in grid[:, col]:
        return False
    box_row_start = box_start(row)
    box_col_start = box_start(col)
    if (
        digit
        in grid[box_row_start : box_row_start + 3, box_col_start : box_col_start + 3]
    ):
        return False
    return True
