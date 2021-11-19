inputFile = open("Day10_Adapter_Array/Input.txt","r")
Lines = inputFile.readlines()

def clean_input():
    input_list = []
    for line in Lines:
        currentInput = line.strip()
        input_list.append(currentInput)
    input_list = list(map(int, input_list))
    input_list.sort()
    return input_list

def question_one():
    """
    What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?
    """
    
    one_jolt_differences = 0
    three_jolt_differences = 0
    current_index = 1

    for value in input_list:
        if current_index ==len(input_list):
            solution = one_jolt_differences*(three_jolt_differences+1)
            print(f"The solution is: {solution}")
            return solution

        current_diff = int(input_list[current_index])-int(value)
        print(f"{int(input_list[current_index])},{int(value)},{current_diff} | 1_diffs: {one_jolt_differences}|3_diffs: {three_jolt_differences}")

        if current_diff == 1:
            one_jolt_differences +=1
        elif current_diff == 3:
            three_jolt_differences +=1

        current_index +=1

input_list = clean_input()
question_one()