"""
inputFile = open("Day11_SeatingSystem/InputTest2.txt","r")
Lines = inputFile.readlines()

input_list = []
for line in Lines:
    currentInput = line.strip()
    input_list.append(currentInput)
for row_number in range(len(input_list)):
    print(row_number)

for row_number in range(len(input_list[0])):
    print(row_number)


print(len(input_list))

#print(len(input_list[0]))
"""
## TEST 2
def find_number_occupied_seats(input_list):
    counter_occupied_seats = 0
    for row_number in range(len(input_list)):
        for column_number in range(len(input_list[0])):
            if current_layout[row_number][column_number]=="#":
                counter_occupied_seats = counter_occupied_seats+1
    return counter_occupied_seats


#current_layout = ['#.##.', 'LL##L', 'L##.L', 'LLLL.']
#print(find_number_occupied_seats(current_layout))

## TEST 3
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
        return current_layout[row_position][column_position]

current_layout = [['#', '#', '#'], ['#', '.', '.'], ['#', '.', '#']]
max_row = int(len(current_layout))
max_column = int(len(current_layout[0]))
print(max_row)
print(max_column)

#print(next_state(current_layout,2,2,2,2))

for row_number in range(len(current_layout)):
    for column_number in range(len(current_layout[0])):
        print(f"Current datapoint is: row_number: {row_number} & column_number: {column_number}")
        new_value = next_state(current_layout,row_number,column_number,max_row,max_column)
        print(new_value)