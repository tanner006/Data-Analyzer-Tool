# Arif Aziz, Tanner Farkas , Meagan Pitts, Jason Dmello

from T078_M2_sort_plot import *
from T078_M1_load_data import *
from T078_M3_optimization import *


student_keys = ['School', 'Age', 'Failures', 'Health']
student_attrs_all = ['School', 'Age', 'StudyTime', 'Failures',
                     'Health', 'Absences', 'G1', 'G2', 'G3', 'G_Avg']
student_attrs_hist = ['School', 'Age',
                      'Health', 'Failures']
student_attrs_rank = ['Age', 'StudyTime', 'Failures',
                      'Health', 'Absences']
#student_dict = {}


def load_menu() -> dict:
    """
    The function prompts the user for entering the file name to load the student
    data and the attribute to load the data with.
    """
    file_name = input("Please enter the name of the file: ")
    key_attr = input(
        "Please enter the attribute to use as key\nValid keys are: 'School', 'Age', 'Failures', 'Health': ")
    while key_attr not in student_keys:
        print("Please enter a valid key. Valid keys are: 'School', 'Age', 'Failures', 'Health'")
        key_attr = input("Please enter the attribute to use as key: ")
    student_dict = add_average(load_data(file_name, key_attr))
    # print(student_dict)
    return student_dict


def sort_menu(student_dict: dict):
    """
    The function prompts for user input for the student attribute for 
    the sorting and then calls the bubble sort function. Once sorted, the
    user will be prompted prompted if the sorted list should be printed. 
    The function will loop until the correct input is entered by the user.
    Precondition: student_dict is a dictionary of students
    """
    msg_part_1 = "Please enter the attribute you want to use for sorting:\n"
    msg_part_2 = "'School' 'Age' 'StudyTime' 'Failures' 'Health' 'Absences' 'G1' 'G2' 'G3' 'G_Avg': "
    sort_key = input(msg_part_1 + msg_part_2)
    while sort_key not in student_attrs_all:
        print("Please enter a valid attribute. Valid attributes are: " + msg_part_2)
        sort_key = input(msg_part_1 + msg_part_2)
    sorted_list = sort_students_bubble(student_dict, sort_key)
    print_sorted = input(
        "Data Sorted. Do you want to display the data? Y or N : ")
    while print_sorted != 'Y' and print_sorted != 'y' and print_sorted != 'N' and print_sorted != 'n':
        print("Please enter Y or N")
        print_sorted = input("Do you want to display the data? Y or N: ")

    if print_sorted == 'Y' or print_sorted == 'y':
        count = 1
        print("---[")
        for e in sorted_list:
            print(count, ") ", e, sep="")
            count += 1
        print("]---")


def hist_menu(student_dict: dict):
    """
    The function prompts for user input for the student attribute for 
    the histogram and then calls the histogram function.
    The function will loop until the correct input is entered by the user.
    Precondition: student_dict is a dictionary of students
    """
    msg_part_1 = "Please enter the attribute you want to use for the historgram:\n"
    msg_part_2 = "'School', 'Age', 'Failures', 'Health':  "
    hist_key = input(msg_part_1 + msg_part_2)
    while hist_key not in student_attrs_hist:
        print("Please enter a valid attribute. Valid attributes are: " + msg_part_2)
        hist_key = input(msg_part_1 + msg_part_2)
    histogram(student_dict, hist_key)


def rank_menu(student_dict: dict, rank: str):
    """
    The function prompts for user input for the student attribue for worst and
    best menu and then calls the maximun or the minimum function.
    The function will loop until the correct input is entered by the user.
    Precondition: student_dict is a dictionary of students and rank is either
    worst or best
    """
    msg_part_1 = ""
    msg_part_3 = ""
    msg_part_4 = ""
    if rank == "worst":
        msg_part_1 = "Please enter the attribute you want to calculate the worse value of the attribute for in terms of grades\n"
        msg_part_3 = "The worst value for the attribute "
    elif rank == "best":
        msg_part_1 = "Please enter the attribute you want to calculate the best value of the attribute for in terms of grades\n"
        msg_part_3 = "The best value for the attribute "

    msg_part_2 = "'Age', 'StudyTime', 'Failures', 'Health', 'Absences' : "

    rank_key = input(msg_part_1 + msg_part_2)
    while rank_key not in student_attrs_rank:
        print("Please enter a valid attribute. Valid attributes are: " + msg_part_2)
        rank_key = input(msg_part_1 + msg_part_2)

    if(rank_key == student_attrs_rank[0]):  # age
        msg_part_4 = " years old"
    elif(rank_key == student_attrs_rank[1]):  # studytime
        msg_part_4 = " hours"
    elif(rank_key == student_attrs_rank[2]):  # failures
        msg_part_4 = " failures"
    elif(rank_key == student_attrs_rank[3]):  # health
        msg_part_4 = ""
    elif(rank_key == student_attrs_rank[4]):  # absences
        msg_part_4 = " absences"

    val = -1
    if rank == "worst":
        val = minimum(student_dict, rank_key)
    elif rank == "best":
        val = maximum(student_dict, rank_key)
    print(msg_part_3, rank_key, " is ", val, msg_part_4)


def print_menu() -> tuple:
    """
    The function prints the main menu of the UI
    Precondition: None
    Examples:
    >>> print_menu()
    The available commands are:
        1. L)oad Data
        2. S)ort Data
                'School' 'Age' 'Failures' 'Health'
                'Absences' 'G1' 'G2' 'G3' 'G_Avg'
        3. H)istogram
                'School' 'Age' 'Failures' 'Health'
        4. W)orst _____ for Grades
                'Age' 'StudyTime' 'Failures' 'Health' 'Absences'
        5.B)est _____forGrades
                'Age' 'StudyTime' 'Failures' 'Health' 'Absences'
        6. Q)uit
    """
    print("The available commands are:")
    print("\t1. L)oad Data")
    print("\t2. S)ort Data")
    print("\t\t'School' 'Age' 'Failures' 'Health'")
    print("\t\t'Absences' 'G1' 'G2' 'G3' 'G_Avg'")
    print("\t3. H)istogram")
    print("\t\t'School' 'Age' 'Failures' 'Health'")
    print("\t4. W)orst _____ for Grades")
    print("\t\t'Age' 'StudyTime' 'Failures' 'Health' 'Absences'")
    print("\t5.B)est _____forGrades")
    print("\t\t'Age' 'StudyTime' 'Failures' 'Health' 'Absences'")
    print("\t6. Q)uit")


if __name__ == "__main__":
    # Main Script
    command = ""
    top_command_list = ["L", "l", "S", "s",
                        "H", "h", "w", "W", "B", "b", "q", "Q"]
    student_dict = {}
    while command != "Q" and command != "q":
        print_menu()
        command = input("Please type your command: ")

        if(not student_dict and command not in top_command_list):
            print("No such command\n")
            continue
        elif(not not student_dict and command not in top_command_list):
            print("Invalid Command")
            continue
        if command == "L" or command == "l":
            student_dict = load_menu()

        if not not student_dict:
            if command == "S" or command == "s":
                sort_menu(student_dict)
            elif command == "H" or command == "h":
                hist_menu(student_dict)
            elif command == "W" or command == "w":
                rank_menu(student_dict, "worst")
            elif command == "B" or command == "b":
                rank_menu(student_dict, "best")

        elif not student_dict and (command != "Q" or command == "q"):
            print("File not loaded. Please, load a file first.\n")
