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


def test_q1():
    with open("Day12_RainRisk/Input.txt") as input:
        inputLines = [str(line.strip()) for line in input]
    assert 2270 == Day12.q1(inputLines)
