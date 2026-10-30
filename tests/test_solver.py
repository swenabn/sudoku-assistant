import numpy as np

from sudoku_assistant.grid import find_empty_cell
from sudoku_assistant.solver import solve

GRID = np.array(
    [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
)


def test_grid_filled() -> None:
    GRID_bis = GRID.copy()
    solve(GRID_bis)
    assert find_empty_cell(GRID_bis) is None


def test_grid_rows_filled() -> None:
    GRID_bis = GRID.copy()
    solve(GRID_bis)
    for row in GRID_bis:
        assert np.array_equal(np.sort(row), np.arange(1, 10))


def test_grid_columns_filled() -> None:
    GRID_bis = GRID.copy()
    solve(GRID_bis)
    for columns in GRID_bis.T:
        assert np.array_equal(np.sort(columns), np.arange(1, 10))


def test_grid_blocks_filled() -> None:
    GRID_bis = GRID.copy()
    solve(GRID_bis)
    for block_index in range(9):
        row_start = (block_index // 3) * 3
        col_start = (block_index % 3) * 3
        block = GRID_bis[row_start : row_start + 3, col_start : col_start + 3]
        assert np.array_equal(np.sort(block.flatten()), np.arange(1, 10))
