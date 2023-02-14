inputFile = open("Day9_EncodingErrors/Input.txt", "r")
Lines = inputFile.readlines()


input_list = []
for line in Lines:
    currentInput = line.strip()
    input_list.append(currentInput)


def q1(preamble_size):
    """
    Find the first number in the list (after the preamble) which is not the 
    sum of two of the 25 numbers before it.
    """
    preamble = []
    rowCounter = 0

    # Create initial preamble
    while rowCounter < preamble_size:
        preamble.append(input_list[rowCounter])
        rowCounter += 1

    while rowCounter < len(input_list):
        valueToGet = input_list[rowCounter]
        if sumPreambleEqualsValueToGet(preamble, valueToGet):
            rowCounter += 1
            preamble.append(valueToGet)
            preamble.pop(0)
        else:
            print(f"Here is the number for Q1: {valueToGet}")
            return valueToGet


def sumPreambleEqualsValueToGet(preamble, valueToGet):
    print(f"The preamble is: {preamble}")
    print(f"The valueToGet is: {valueToGet}")
    for x in range(len(preamble)):
        for y in range(len(preamble)):
            valueX = int(preamble[x])
            valueY = int(preamble[y])
            # print(f"Here is ValueX and ValueY: {valueX} and {valueY}")
            if ((valueX+valueY) == int(valueToGet) and (valueX != valueY)):
                print(
                    f"Found a solution with the sum of {valueX} and {valueY}")
                return True

    # if you haven't found any results, return False
    return False


# q1(5)
# Results for TEST input: 127
# Results for REAL input: 3199139634

NUMBER_TO_FIND = 3199139634


def question_two_recursive(pointer_high_boundery, current_list, current_sum):
    # print(f"{pointer_high_boundery},{current_list},{current_sum}")

    if current_list == []:
        current_list.append(input_list[pointer_high_boundery])
        current_sum += int(input_list[pointer_high_boundery])
        pointer_high_boundery += 1
        question_two_recursive(pointer_high_boundery,
                               current_list, current_sum)

    else:
        if current_sum < NUMBER_TO_FIND:
            current_list.append(input_list[pointer_high_boundery])
            current_sum += int(input_list[pointer_high_boundery])
            pointer_high_boundery += 1
            question_two_recursive(pointer_high_boundery,
                                   current_list, current_sum)
        elif current_sum > NUMBER_TO_FIND:
            current_sum -= int(current_list.pop(0))
            question_two_recursive(pointer_high_boundery,
                                   current_list, current_sum)
        else:
            solution = int(min(current_list)) + int(max(current_list))
            print(f"SOLUTION: {solution}")


# print(question_two_recursive(0, [],0))
# Fails with: RecursionError: maximum recursion depth exceeded in comparison

def question_two_iterative(pointer_high_boundery, current_list, current_sum, solution_found):
    # print(f"{pointer_high_boundery},{current_list},{current_sum}")

    if current_list == []:
        current_list.append(input_list[pointer_high_boundery])
        current_sum += int(input_list[pointer_high_boundery])
        pointer_high_boundery += 1
        return(pointer_high_boundery, current_list, current_sum, solution_found)

    else:
        if current_sum < NUMBER_TO_FIND:
            current_list.append(input_list[pointer_high_boundery])
            current_sum += int(input_list[pointer_high_boundery])
            pointer_high_boundery += 1
            return(pointer_high_boundery, current_list, current_sum, False)
        elif current_sum > NUMBER_TO_FIND:
            current_sum -= int(current_list.pop(0))
            return(pointer_high_boundery, current_list, current_sum, False)
        else:
            solution = int(min(current_list)) + int(max(current_list))
            print(f"SOLUTION: {solution}")
            return(0, [], 0, True)


def question_two_iterative_helper():
    solution_found = False
    pointer_high_boundery = 0
    current_list = []
    current_sum = 0

    while solution_found == False:
        pointer_high_boundery, current_list, current_sum, solution_found = question_two_iterative(
            pointer_high_boundery, current_list, current_sum, solution_found)


question_two_iterative_helper()
