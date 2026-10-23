from sudoku_assistant.grid import box_start


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
