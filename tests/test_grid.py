import numpy as np

from sudoku_assistant.grid import box_start, find_empty_cell, is_valid_placement

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

ONES_GRID = np.ones((9, 9))


def test_box_start_first_box() -> None:
    assert box_start(0) == 0
    assert box_start(1) == 0
    assert box_start(2) == 0


def test_box_start_second_box() -> None:
    assert box_start(3) == 3
    assert box_start(4) == 3
    assert box_start(5) == 3


def test_box_start_third_box() -> None:
    assert box_start(6) == 6
    assert box_start(7) == 6
    assert box_start(8) == 6


def test_rejects_digit_in_row() -> None:
    assert not is_valid_placement(GRID, 0, 2, 5)


def test_rejects_digit_in_column() -> None:
    assert not is_valid_placement(GRID, 4, 1, 9)


def test_rejects_digit_in_box() -> None:
    assert not is_valid_placement(GRID, 0, 2, 6)


def test_accepts_valid_digit() -> None:
    assert is_valid_placement(GRID, 2, 5, 4)


def test_find_first_empty_cell() -> None:
    assert find_empty_cell(GRID) == (0, 2)


def test_find_full_grid() -> None:
    assert find_empty_cell(ONES_GRID) is None
