import Day11

def test_find_number_occupied_seats_1():
    assert 6 == Day11.find_number_occupied_seats([['#', '#', '#'], ['#', '.', '.'], ['#', '.', '#']])

def test_find_number_occupied_seats_2():
    assert 0 == Day11.find_number_occupied_seats([[], [], []])


#class TestNextState:


def test_next_state_1():
    current_layout = [['#', '#', '#'], ['#', '.', '.'], ['#', '.', '#']]
    max_row = int(len(current_layout))-1
    max_column = int(len(current_layout[0]))-1
    assert "." == Day11.next_state(current_layout,1,1,max_row,max_column)
