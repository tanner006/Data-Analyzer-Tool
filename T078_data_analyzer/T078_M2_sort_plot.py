# Arif Aziz, Tanner Farkas , Meagan Pitts, Jason Dmello

from T078_M1_load_data import *
import matplotlib.pyplot as plt
import numpy as np

# ======================================================
# 1 student_list


def student_list(s_dict: dict) -> list:
    """
    The function copies the s_dict dictionary and then collects all values of each key and
    inserts it into a list
    Precondition: s_dict is a student dictionary of appropriate format
    such as {1: [{'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Absences': 6, 'G1': 6, 'G2': 5, 'G3': 6},{another element}, ...]...}
    Example
    >>> student_list({1: [{'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Absences': 6, 'G1': 6, 'G2': 5, 'G3': 6},{another element}, ...]...})
    [{'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Absences': 6, 'G1': 6, 'G2': 5, 'G3': 6, Health:1}, {another element},...]
    """
    possible_keys = ["School", "Failures",
                     "Health", "Age"]

    # copy the keys and insert empty lists
    s_dict_copy = s_dict.copy()
    for key in s_dict_copy:
        s_dict_copy[key] = []

    # copy all the inner dictionary
    for key, values in s_dict.items():
        innerdict_copy = {}
        for v in values:
            innerdict_copy = v.copy()
            s_dict_copy[key].append(innerdict_copy)
    # populate the s_list with inner dictionary and the missing key
    # without changing the s_dict parameter passed the method
    s_list = []
    for key, values in s_dict_copy.items():
        # inner_dict = values.copy()
        for v in values:
            missing_key = possible_keys - v.keys()
            if not not missing_key:
                v[list(missing_key)[0]] = key
            s_list.append(v)
    return s_list


# ======================================================
# 2 sort_students_bubble

def sort_students_bubble(dictionary: dict, attribute: str) -> list:
    """ The function creates a list with the student data and then uses the bubble sort algorithm for sorting the list of students by the attribute indicated in the input string (schools by alphabetical order and all other attrubutes in ascending numerical order). The function will return a sorted list with the student data stored as individual dictionaries.

    Preconditions: attribute must be one of the keys in the dictionary and the dictionary must exist globally (outside of the function).

    >>> sort_students_bubble(s_dict, "Health")
    [{'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Health': 1, 'Absences': 6, 'G1': 6, 'G2': 5, 'G3': 6}, ... , 'Health': 2, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14}, {'Age': 16, 'StudyTime': 3, 'Failures': 0, 'Health': 2, 'Absences': 6, 'G1': 13, 'G2': 14, 'G3': 14}, {'Age': 15, 'StudyTime': 2, 'Failures': 0, 'Health': 2, 'Absences': 0, 'G1': 8, 'G2': 10, 'G3': 12}, ... ,{'Age': 15, 'StudyTime': 4, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 13, 'G2': 13, 'G3': 12}, {'Age': 15, 'StudyTime': 4, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 16, 'G2': 16, 'G3': 16}, {'Age': 15, 'StudyTime': 4, 'Failures': 0, 'Health': 3, 'Absences': 0, 'G1': 10, 'G2': 10, 'G3': 10}, {'Age': 19, 'StudyTime': 1, 'Failures': 1, 'Health': 4, 'Absences': 38, 'G1': 8, 'G2': 9, 'G3': 8}, ... , {'Age': 19, 'StudyTime': 2, 'Failures': 1, 'Health': 4, 'Absences': 3, 'G1': 13, 'G2': 11, 'G3': 11}, {'Age': 17, 'StudyTime': 1, 'Failures': 0, 'Health': 4, 'Absences': 8, 'G1': 11, 'G2': 10, 'G3': 10}, {'Age': 17, 'StudyTime': 3, 'Failures': 0, 'Health': 4, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9}, {'Age': 17, 'StudyTime': 3, 'Failures': 0, 'Health': 4, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14}, {'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 4, 'Absences': 0, 'G1': 7, 'G2': 0, 'G3': 0}, {'Age': 18, 'StudyTime': 4, 'Failures': 0, 'Health': 4, 'Absences': 0, 'G1': 10, 'G2': 9, 'G3': 0}, {'Age': 17, 'StudyTime': 2, 'Failures': 1, 'Health': 4, 'Absences': 0, 'G1': 9, 'G2': 8, 'G3': 0}, ... , {'Age': 15, 'StudyTime': 1, 'Failures': 1, 'Health': 5, 'Absences': 6, 'G1': 11, 'G2': 11, 'G3': 10}, {'Age': 15, 'StudyTime': 1, 'Failures': 0, 'Health': 5, 'Absences': 0, 'G1': 8, 'G2': 10, 'G3': 11}, ...]
    """
    list_to_sort = student_list(dictionary)

    swap = True
    while swap:
        swap = False
        for i in range(len(list_to_sort) - 1):
            val_of_attribute = list_to_sort[i].get(attribute)
            val_of_attribute_ahead = list_to_sort[i + 1].get(attribute)

            if val_of_attribute > val_of_attribute_ahead:
                # swap
                aux = list_to_sort[i]
                list_to_sort[i] = list_to_sort[i + 1]
                list_to_sort[i + 1] = aux
                swap = True
    return(list_to_sort)


# ======================================================
# 3 sort_students_selection
def sort_students_selection(s_dict: dict, category: str) -> list:
    """
    Returns a sorted list of students based on the category outlined in the input string. It will be sorted in ascending numerical order for number lists, for alphabetical lists it will be sorted alphabetically.

    Examples:
    >>>sort_students_selection(s_dict, 'Age')
    [{'School': 'GP', 'StudyTime': 15, 'Failures': 2, 'Health': 3, 'Absences': 3, 'G1': 10, 'G2': 7, 'G3': 8, 'Age': 15}, {'School': 'GP', 'StudyTime': 15, 'Failures': 3, 'Health': 0, 'Absences': 5, 'G1': 2, 'G2': 15, 'G3': 14, 'Age': 15},...]

    """
    list_of_students = student_list(s_dict)

    for i in range(len(list_of_students)):
        min_index = i
        sort_method = category

        for j in range(i + 1, len(list_of_students)):
            if list_of_students[min_index][sort_method] > list_of_students[j][sort_method]:
                min_index = j
                list_of_students[i], list_of_students[min_index] = list_of_students[min_index], list_of_students[i]

    return list_of_students


# ======================================================
# 4 curve_fit
def curve_fit(s_dict: dict, s_attr: str, order: int) -> list:
    """
    The function takes three input pratmeters
    a dictionary of students including the G_Avg,
    a string indicating the attribute to which grades will be compared,
    a integer indicating the degree of the polynomial between 1 and 5,
    and
    if the degree is not within range (1 to 5inclusive)
    the function will do interpolation instead of regression
    The function returns equation of the best fit curve as a list of
    coefficients
    Precondition:
    s_dict should be a dictionary of students
    s_attr should be a student attribute in the s_dict with numerical values
    order should be in the range of 1 to 5 inclusive
    Example
    >>>curve_fit()
    """
    G_AVG_KEY = "G_Avg"
    G1_KEY = "G1"
    G2_KEY = "G3"
    G3_KEY = "G3"

    z = []
    s_list = student_list(s_dict)

    # create the data as a tuple (average, count) and save it in a dict
    # keyed by the s_attr value
    # data in : s_list, s_attr
    # data out: s_attr_dict = {s_attr_val : (avg, count)...},
    #
    # load_data_key: the key used to retrieve the student information
    #                usually the last key of the s_list
    s_attr_dict = {}
    load_data_key = list(s_list[0])[-1]
    for stdnt_attr_inner_dict in s_list:
        s_attr_value = stdnt_attr_inner_dict[s_attr]

        g1_value = stdnt_attr_inner_dict[G1_KEY]
        g2_value = stdnt_attr_inner_dict[G2_KEY]
        g3_value = stdnt_attr_inner_dict[G3_KEY]
        g_avg_value = (g1_value + g2_value + g3_value) / 3

        if s_attr_value in s_attr_dict.keys():
            curr_avg, sum_amount, count = s_attr_dict[s_attr_value]
            new_count = count + 1
            new_sum_amount = sum_amount + g_avg_value
            new_avg = (new_sum_amount) / new_count
            s_attr_dict[s_attr_value] = (new_avg, new_sum_amount, new_count)
        else:
            s_attr_dict[s_attr_value] = (g_avg_value, g_avg_value, 1)

    # creating the lists for the plot
    x_list = [i for i in s_attr_dict.keys()]
    y_list = []
    for x_val in x_list:
        avg_val, _, count = s_attr_dict[x_val]
        y_list.append(avg_val)

    # now we can plot but here the conditions to plot
    # The degree of the polynomial is defined by the integer provided as input.
    # Remember: if the order provided is higher than the interpolating
    # polynomial, you should do interpolation instead of regression.
    # order of the interpolating polynomial is always given by
    # the number of x values -1
    fig = plt.figure()

    # we need to do interpolation when the x_list contains elements more
    # than 5, or when user given order is not with 1 and 5 inclusive or when
    # order is greater than the polynomial degree
    if (len(x_list) - 1 >= 5) or order < 1 or order >= 5 or order > len(x_list) - 1:
        z = np.polyfit(x_list, y_list, len(x_list) - 1)
        plt.scatter(x_list, y_list)
        plt.title("Polynomial interpolation loaded with " + load_data_key)
        plt.xlabel(s_attr)
        plt.ylabel('Grade Average')
    else:  # we need to do regression
        z = np.polyfit(x_list, y_list, order)
        x_e = np.linspace(min(x_list), max(x_list), 100)
        y_e = np.polyval(z, x_e)

        plt.plot(x_list, y_list, 'o', x_e, y_e, '-')
        plt.title("Polynomial regression loaded with " +
                  load_data_key + " of order " + str(order))
        plt.xlabel(s_attr)
        plt.ylabel('Grade Average')
    # lets plot now \o/
    plt.show()
    return z


# ======================================================
# 5 histogram
def histogram(loaded_dict: dict, attribute: str) -> None:
    """
    The function will plot and show the histogram. The function will return None.
    The function has two input parameters: a dictionary (any of the ones generated by the Load Data module), and a string. 
    The string will indicate what attribute will be plotted. The function will convert the student data to a list using the function student_list.
    Then, the function will go through all students and store the number of students that are at each level of the attribute.
    This data will then be used to plot a histogram.
    Preconditions: Parameter 1 expects input be of type 'dict', and parameter 2 expects input of type 'str'.
    For example; if the attribute is ‘health’, it will store the number of students with each of ‘health’:1, ‘health’: 2, etc. 
    """
    count_school_GP = 0
    count_school_MB = 0
    count_school_CF = 0
    count_school_BD = 0
    count_school_MS = 0
    count_health_1 = 0
    count_health_2 = 0
    count_health_3 = 0
    count_health_4 = 0
    count_health_5 = 0
    count_age_15 = 0
    count_age_16 = 0
    count_age_17 = 0
    count_age_18 = 0
    count_age_19 = 0
    count_age_20 = 0
    count_age_21 = 0
    count_age_22 = 0
    count_fail_1 = 0
    count_fail_2 = 0
    count_fail_3 = 0
    count_fail_4 = 0
    count_fail_5 = 0
    count_fail_6 = 0
    count_fail_7 = 0
    count_fail_8 = 0
    count_fail_9 = 0
    count_fail_10 = 0
    new_list = student_list(loaded_dict)
    if attribute == "School":
        for entry in new_list:
            if attribute in entry:
                if entry.get('School') == 'GP':
                    count_school_GP += 1
                elif entry.get('School') == 'MB':
                    count_school_MB += 1
                elif entry.get('School') == 'CF':
                    count_school_CF += 1
                elif entry.get('School') == 'BD':
                    count_school_BD += 1
                elif entry.get('School') == 'MS':
                    count_school_MS += 1
        schools = ['GP', 'MB', 'CF', 'BD', 'MS']
        values = [count_school_GP, count_school_MB,
                  count_school_CF, count_school_BD, count_school_MS]
        fig = plt.figure(figsize=(10, 5))

        # creating the bar plot
        plt.bar(schools, values, color='red',
                width=0.4)

        plt.xlabel("Schools")
        plt.ylabel("No. of students enrolled")
        plt.title("Students enrolled in different schools")
        plt.show()
    if attribute == "Health":
        for entry in new_list:
            if attribute in entry:
                if entry.get('Health') == 1:
                    count_health_1 += 1
                elif entry.get('Health') == 2:
                    count_health_2 += 1
                elif entry.get('Health') == 3:
                    count_health_3 += 1
                elif entry.get('Health') == 4:
                    count_health_4 += 1
                elif entry.get('Health') == 5:
                    count_health_5 += 1
        health = list(range(1, 6))
        values = [count_health_1, count_health_2,
                  count_health_3, count_health_4, count_health_5]
        fig = plt.figure(figsize=(10, 5))

        # creating the bar plot
        plt.bar(health, values, color='red',
                width=0.4)

        plt.xlabel("Health")
        plt.ylabel("No. of students at level")
        plt.title("Students enrolled at different health levels")
        plt.show()
    if attribute == "Age":
        for entry in new_list:
            if attribute in entry:
                if entry.get('Age') == 15:
                    count_age_15 += 1
                elif entry.get('Age') == 16:
                    count_age_16 += 1
                elif entry.get('Age') == 17:
                    count_age_17 += 1
                elif entry.get('Age') == 18:
                    count_age_18 += 1
                elif entry.get('Age') == 19:
                    count_age_19 += 1
                elif entry.get('Age') == 20:
                    count_age_20 += 1
                elif entry.get('Age') == 21:
                    count_age_21 += 1
                elif entry.get('Age') == 22:
                    count_age_22 += 1
        ages = list(range(15, 23))
        values = [count_age_15, count_age_16, count_age_17, count_age_18,
                  count_age_19, count_age_20, count_age_21, count_age_22, ]
        fig = plt.figure(figsize=(10, 5))

        # creating the bar plot
        plt.bar(ages, values, color='red',
                width=0.4)

        plt.xlabel("Ages")
        plt.ylabel("No. of students at each age")
        plt.title("Students enrolled for different ages")
        plt.show()
    if attribute == "Failures":
        for entry in new_list:
            if attribute in entry:
                if entry.get('Failures') == 1:
                    count_fail_1 += 1
                elif entry.get('Failures') == 2:
                    count_fail_2 += 1
                elif entry.get('Failures') == 3:
                    count_fail_3 += 1
                elif entry.get('Failures') == 4:
                    count_fail_4 += 1
                elif entry.get('Failures') == 5:
                    count_fail_5 += 1
                elif entry.get('Failures') == 6:
                    count_fail_6 += 1
                elif entry.get('Failures') == 7:
                    count_fail_7 += 1
                elif entry.get('Failures') == 8:
                    count_fail_8 += 1
                elif entry.get('Failures') == 9:
                    count_fail_9 += 1
                elif entry.get('Failures') == 10:
                    count_fail_10 += 1
        failures = list(range(0, 10))
        values = [count_fail_1, count_fail_2, count_fail_3, count_fail_4, count_fail_5,
                  count_fail_6, count_fail_7, count_fail_8, count_fail_9, count_fail_10]
        fig = plt.figure(figsize=(10, 5))

        # creating the bar plot
        plt.bar(failures, values, color='red',
                width=0.4)

        plt.xlabel("Failures")
        plt.ylabel("No. of students at each failure level")
        plt.title("Students enrolled for different number of failures")
        plt.show()


if __name__ == "__main__":
    # calling function 2
    # any arguement assumed to be a function from the previously built load_data function will work.
    s_dict = load_data("student-mat.csv", "School")
    # "Health" can be replaced with any defined key from the dictionary
    sorted_list = sort_students_bubble(s_dict, "Health")

    # calling function 3
    s_dict = student_age_dictionary('student-mat.csv')
    sorted_list = sort_students_selection(s_dict, 'Age')

    # calling function 4
    z = curve_fit(load_data("student-mat.csv", "School"), "Failures", 1)
    z = curve_fit(load_data("student-mat.csv", "Age"), "Failures", 2)
    z = curve_fit(add_average(
        load_data("student-mat.csv", "Health")), "Failures", 3)

    z = curve_fit(add_average(
        load_data("student-mat.csv", "School")), "Age", 1)
    z = curve_fit(add_average(
        load_data("student-mat.csv", "Failures")), "Age", 2)
    z = curve_fit(add_average(
        load_data("student-mat.csv", "Health")), "Age", 3)

    z = curve_fit(add_average(
        load_data("student-mat.csv", "School")), "Health", 1)
    z = curve_fit(add_average(
        load_data("student-mat.csv", "Failures")), "Health", 2)
    z = curve_fit(add_average(
        load_data("student-mat.csv", "Age")), "Health", 3)

    # calling function 5
    s_dict = load_data("student-mat.csv", "School")

    histogram(s_dict, "School")
    histogram(s_dict, "Age")
    histogram(s_dict, "Failures")
    histogram(s_dict, "Health")





