# authors: Tanner Farkas, Meagan Pitts, Arif Aziz, Jason Dmello

from T078_M1_load_data import *
from T078_M2_sort_plot import *
from scipy.optimize import *
import matplotlib.pyplot as plt
import numpy as np


def curve_fit(s_dict: dict, s_attr: str, order: int) -> tuple:
    """
    The function takes three input parameters
    a dictionary of students including the G_Avg,
    a string indicating the attribute to which grades will be compared,
    a integer indicating the degree of the polynomial between 1 and 5,
    and
    if the degree is not within range (1 to 5inclusive)
    the function will do interpolation instead of regression
    The function returns a tuple with the first item in the tuple being the equation of the best fit curve as a list of coefficients. The second item in the tuple is a list with the minimum and maximum x value (i.e the domain borders of the second order function).
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

    # The degree of the polynomial is defined by the integer provided as input.
    # Remember: if the order provided is higher than the interpolating
    # polynomial, you should do interpolation instead of regression.
    # order of the interpolating polynomial is always given by
    # the number of x values -1

    # we need to do interpolation when the x_list contains elements more
    # than 5, or when user given order is not with 1 and 5 inclusive or when
    # order is greater than the polynomial degree
    if (len(x_list) - 1 >= 5) or order < 1 or order >= 5 or order > len(x_list) - 1:
        z = np.polyfit(x_list, y_list, len(x_list) - 1)

    else:  # we need to do regression
        z = np.polyfit(x_list, y_list, order)

    interval = [min(x_list), max(x_list)]

    return (z, interval)


def minimum(dictionary: dict, attribute: str) -> tuple:
    """
    Returns the x and y values for the local minimum value that is contained in the domain of the second order function. Given dict (a dictionary loaded from the load_data module) and attribute (a string which is the name of a key from the dictionary).

    Precondition: attribute must be a name of a key from the dictionary and must differ from the load_data second parameter (For example: if the dictionary is load_data("student-mat.csv", "School"), the attribute must not be "School".

    >>> minimum(load_data("student-mat.csv", "School"),"Failures")
    """
    function_data = curve_fit(dictionary, attribute, 2)
    coef, interval = function_data  # unpack tuple

    def func(x: float) -> float:
        """ Returns an evaluated polynomial at point x using coef (equation of the best fit curve as a list of coefficients)

        Precondition: len(coef > 0)

        >>>func(x)
        """
        return np.polyval(coef, x)

    interval_one = interval[0]
    interval_two = interval[1]
    x_val = fminbound(func, interval_one, interval_two)
    y_val = func(x_val)
    return x_val, y_val


def maximum(dictionary: dict, string: str) -> tuple:
    """
    Returns a tuple with the x and y values of the local maximum between the lowest and highest value of the attrivute.
    Precondition: attribute must be a name of a key from the dictionary and must differ from the load_data second parameter (For example: if the dictionary is load_data("student-mat.csv", "Health"), the attribute must not be "Healthl".

    Example:
    >>> maxmimum(load_data("student-mat.csv", "Health"),"Age")
    """
    z, L = curve_fit(dictionary, string, 2)

    def quad(x: float) -> float:
        """
        Creates a quadratic function
        """
        return -z[0] * x**2 - z[1] * x - z[2]
    x_max = fminbound(quad, L[0], L[1])
    y_max = quad(x_max)
    return(x_max, y_max)


# main script
if __name__ == "__main__":
    minimum(load_data("student-mat.csv", "School"), "Failures")

    minimum(load_data("student-mat.csv", "Age"), "Failures")

    minimum(add_average(
        load_data("student-mat.csv", "Health")), "Failures")

    minimum(add_average(
        load_data("student-mat.csv", "School")), "Age")

    minimum(add_average(
        load_data("student-mat.csv", "Failures")), "Age")

    minimum(add_average(
        load_data("student-mat.csv", "Health")), "Age")

    minimum(add_average(
        load_data("student-mat.csv", "School")), "Health")

    minimum(add_average(
        load_data("student-mat.csv", "Failures")), "Health")

    minimum(add_average(
        load_data("student-mat.csv", "Age")), "Health")

    maximum(load_data('student-mat.csv', 'School'), 'Failures')

    maximum(load_data('student-mat.csv', 'Age'), 'Failures')

    maximum(add_average(load_data('student-mat.csv', 'Health')), 'Age')

    maximum(add_average(load_data('student-mat.csv', 'Failures')), 'Age')

    maximum(add_average(load_data('student-mat.csv', 'Health')), 'Age')

    maximum(add_average(load_data('student-mat.csv', 'School')), 'Health')

    maximum(add_average(load_data('student-mat.csv', 'Failures')), 'Health')

    maximum(add_average(load_data('student-mat.csv', 'Age')), 'Health')
