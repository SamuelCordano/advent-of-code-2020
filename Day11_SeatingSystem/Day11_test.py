import Day11

# Test Common to Q1 &Q2

def test_find_number_occupied_seats_1():
    assert 6 == Day11.find_number_occupied_seats([['#', '#', '#'], ['#', '.', '.'], ['#', '.', '#']])

def test_find_number_occupied_seats_2():
    assert 0 == Day11.find_number_occupied_seats([[], [], []])

# Test specific to Q1
def test_next_state_1():
    current_layout = [['#', '#', '#'], ['#', '.', '.'], ['#', '.', '#']]
    max_row = int(len(current_layout))-1
    max_column = int(len(current_layout[0]))-1
    assert "." == Day11.next_state(current_layout,1,1,max_row,max_column)


def test_q1():
    inputFile = open("Day11_SeatingSystem/InputTest.txt","r")
    Lines = inputFile.readlines()

    input_list = []
    for line in Lines:
        input_line = []
        currentInput = line.strip()
        for character in currentInput:
            input_line.append(character)
        input_list.append(input_line)
    
    assert 37 == Day11.q1(input_list)

# Test specific to Q2

def test_q1():
    inputFile = open("Day11_SeatingSystem/InputTest.txt","r")
    Lines = inputFile.readlines()

    input_list = []
    for line in Lines:
        input_line = []
        currentInput = line.strip()
        for character in currentInput:
            input_line.append(character)
        input_list.append(input_line)
    
    assert 26 == Day11.q2(input_list)