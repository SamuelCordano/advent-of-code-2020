import Day12


def test_changeDirection_1():
    assert "S" == Day12.changeDirection("E", "R90")


def test_changeDirection_2():
    assert "W" == Day12.changeDirection("E", "R180")


def test_changeDirection_3():
    assert "N" == Day12.changeDirection("E", "R270")


def test_changeDirection_4():
    assert "N" == Day12.changeDirection("E", "L90")


def test_changeDirection_5():
    assert "W" == Day12.changeDirection("E", "L180")
