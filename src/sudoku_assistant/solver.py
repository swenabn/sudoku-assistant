import numpy as np

from sudoku_assistant.grid import find_empty_cell, is_valid_placement


def solve(grid: np.ndarray) -> bool:
    """Solve the grid in place. Return True if a solution was found"""
    cell = find_empty_cell(grid)
    if cell is None:  # If the grid is full, then the sudoku is solved
        return True
    else:
        (i, j) = cell
        for digit in range(1, 10):
            if is_valid_placement(grid, i, j, digit):
                grid[i][j] = digit
                if solve(grid):
                    return True
                else:
                    grid[i][j] = 0
        return False
