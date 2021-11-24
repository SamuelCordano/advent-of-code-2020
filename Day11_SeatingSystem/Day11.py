from pprint import pprint
import copy

def next_state(current_layout,row_position,column_position,max_row,max_column):
    """
    Example List of List: 
    [['a', 'b', 'c'], 
    ['d', 'X', 'e'], 
    ['f', 'i', 'j']]
    
    """
    #Check if floor: 
    if current_layout[row_position][column_position]==".":
        return "."
    #Check number of neighboor seats that are occupied
    counter_occupied_neighboors = 0
    #Situation i
    if row_position <max_row: 
        if current_layout[row_position+1][column_position]=="#":
            counter_occupied_neighboors += 1
    #Situation b
    if row_position >0:
        if current_layout[row_position-1][column_position]=="#":
            counter_occupied_neighboors += 1
    #Situation e
    if column_position <max_column: 
        if current_layout[row_position][column_position+1]=="#":
            counter_occupied_neighboors += 1
    #Situation d
    if column_position >0:
        if current_layout[row_position][column_position-1]=="#":
            counter_occupied_neighboors += 1
    
    #Situation j 
    if row_position <max_row and column_position <max_column: 
        if current_layout[row_position+1][column_position+1]=="#":
            counter_occupied_neighboors += 1
    #Situation c
    if row_position <max_row and column_position >0:
        if current_layout[row_position+1][column_position-1]=="#":
            counter_occupied_neighboors += 1
    #Situation f
    if row_position >0 and column_position <max_column: 
        if current_layout[row_position-1][column_position+1]=="#":
            counter_occupied_neighboors += 1
    #Situation a
    if row_position >0 and column_position >0:
        if current_layout[row_position-1][column_position-1]=="#":
            counter_occupied_neighboors += 1

    if current_layout[row_position][column_position]=="L" and counter_occupied_neighboors==0:
        return "#"
    elif current_layout[row_position][column_position]=="#" and counter_occupied_neighboors>3: 
        return "L"
    else: 
        return str(current_layout[row_position][column_position])

def find_number_occupied_seats(current_layout):
    counter_occupied_seats = 0
    for row_number in range(len(current_layout)):
        for column_number in range(len(current_layout[0])):
            if current_layout[row_number][column_number]=="#":
                counter_occupied_seats = counter_occupied_seats+1
    return counter_occupied_seats

def find_next_round_layout(current_layout,max_row,max_column):
    new_layout = copy.deepcopy(current_layout)
    for row_number in range(len(current_layout)):
        for column_number in range(len(current_layout[0])):
            new_value = next_state(current_layout,row_number,column_number,max_row,max_column)
            new_layout[row_number][column_number]=new_value

    return new_layout

def q1(current_layout):
    max_row = int(len(current_layout))-1
    max_column = int(len(current_layout[0]))-1
    counter = 0
    print("Start of Loop ")
    while (True):
        print(f"counter: {counter}")
        new_layout =  copy.deepcopy(current_layout)
        new_layout = copy.deepcopy(find_next_round_layout(new_layout,max_row,max_column))
        if(current_layout == new_layout):
            print("They're equal !!")
            break
        else: 
            current_layout= list(new_layout)
            print("They're NOT equal !!")
        counter+=1

        if counter == 150: 
            break

    
    #Find number of occupied seats
    result_q1 = find_number_occupied_seats(current_layout)
    print(f"The result of question 1 is: {result_q1}")
    return result_q1

if __name__ == "__main__":
    inputFile = open("Day11_SeatingSystem/Input.txt","r")
    Lines = inputFile.readlines()

    input_list = []
    for line in Lines:
        input_line = []
        currentInput = line.strip()
        for character in currentInput:
            input_line.append(character)
        input_list.append(input_line)
    
    #Q1
    q1(input_list)