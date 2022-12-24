# Arif Aziz, Tanner Farkas , Meagan Pitts, Jason Dmello

from T078_M1_load_data import *
from T078_M2_sort_plot import *
from T078_M3_optimization import *


def execute_load_command(new_list: list) -> dict:
    '''
    Returns the loaded data to the batch_process_funtion.
    Precondtions: Assumes that the list is of approprate lenght. 
    '''
    loaded_data = {}
    if new_list[0] == 'L' or new_list[0] == 'l':
        loaded_data = load_data(new_list[1], new_list[2])
        print('Data loaded')
        return loaded_data
    else:
        print('Invalid Input')


def execute_sort_command(dictionary: dict, attribute: list) -> list:
    '''
    Returns a sorted list based on the attributes input.
    Precondtions: Assumes that the dictionary is of type 'dict'.
    Example:
    [{'Age': 15, 'StudyTime': 2, 'Failures': 0, 'Health': 1, 'Absences': 0, 'G1': 16, 'G2': 18, 'G3': 19, 'School': 'GP'},...]

    '''
    sorted_data = sort_students_selection(dictionary, attribute[1])
    return sorted_data


def execute_best_command(dictionary: dict, attribute: list) -> float:
    '''
    Returns a tuple based on the conditions.
    Precondtions: Assumes that dictionary is of type 'dict'
    '''
    best_data = maximum(dictionary, attribute[1])
    x, y = best_data
    return x


def execute_worst_command(dictionary: dict, attribute: list) -> float:
    '''
    Returns a tuple based on the conditions.
    Precondtions: Assumes that dictionary is of type 'dict'
    '''
    worst_data = minimum(dictionary, attribute[1])
    x, y = worst_data
    return x


def batch_process_function(filename: str):
    """
    Returns the results of commands executed from a batch text file porovided by the user.
    The user inputs for the command are not case sensitive, however the attributes/keys to the commands are.
    Preconditions: Assumes that the file contains no errors.
    Examples:
    Please enter the name of the file where your commands are stored :
    ult.txt
    Data loaded
    Data sorted.
    21.99999391225472
    3.5836125919209687
    """
    batch_file = open(filename, "r")
    strip_list = []
    for line in batch_file:
        items = line.split(';')
        for a in items:
            strip_list.append(a.strip())
    loaded_data = execute_load_command(strip_list)
    if loaded_data == {}:
        print('File not loaded. Please, load a file first.')
    else:
        for i in strip_list:
            if 's' in strip_list:
                index = strip_list.index('s')
                sorted_data = execute_sort_command(
                    loaded_data, strip_list[index:index + 2])
            if 'S' in strip_list:
                index = strip_list.index('S')
                sorted_data = execute_sort_command(
                    loaded_data, strip_list[index:index + 2])
            if 'b' in strip_list:
                index = strip_list.index('b')
                best_data = execute_best_command(
                    loaded_data, strip_list[index:index + 2])
            if 'B' in strip_list:
                index = strip_list.index('B')
                best_data = execute_best_command(
                    loaded_data, strip_list[index:index + 2])
            if 'w' in strip_list:
                index = strip_list.index('w')
                worst_data = execute_worst_command(
                    loaded_data, strip_list[index:index + 2])
            if 'W' in strip_list:
                index = strip_list.index('W')
                worst_data = execute_worst_command(
                    loaded_data, strip_list[index:index + 2])
    if 's' in strip_list:
        index = strip_list.index('s')
        if strip_list[index + 2] == 'y':
            print("Data sorted.")
            print(sorted_data)
    if 's' in strip_list:
        index = strip_list.index('s')
        if strip_list[index + 2] == 'Y':
            print("Data sorted.")
            print(sorted_data)
    if 'S' in strip_list:
        index = strip_list.index('s')
        if strip_list[index + 2] == 'y':
            print("Data sorted.")
            print(sorted_data)
    if 'S' in strip_list:
        index = strip_list.index('s')
        if strip_list[index + 2] == 'Y':
            print("Data sorted.")
            print(sorted_data)
    if 'S' in strip_list:
        if strip_list[index + 2] == 'n':
            print('Data sorted')
    if 'S' in strip_list:
        if strip_list[index + 2] == 'N':
            print('Data sorted')
    if 's' in strip_list:
        if strip_list[index + 2] == 'n':
            print('Data sorted')
    if 's' in strip_list:
        if strip_list[index + 2] == 'N':
            print('Data sorted')
    if 'b' in strip_list:
        print(best_data)
    if 'B' in strip_list:
        print(best_data)
    if 'w' in strip_list:
        print(worst_data)
    if 'W' in strip_list:
        print(worst_data)
    if 'h' in strip_list:
        index = strip_list.index('h')
        histogram(loaded_data, strip_list[index + 1])
    if 'H' in strip_list:
        index = strip_list.index('H')
        histogram(loaded_data, strip_list[index + 1])


if __name__ == "__main__":
    filename = input(
        'Please enter the name of the file where your commands are stored :\n')
    batch_process_function(filename)
