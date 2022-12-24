# Arif Aziz, Tanner Farkas , Meagan Pitts, Jason Dmello

import string
from typing import List
from check_equal import check_equal

# ======================================================
# 1


def student_school_dictionary(file: str) -> dict:
    """
    The function reads the 'student-mat.csv' and creates
    a dictionary of students keyed on the school initials
    the student attended. The value of the dictionary is a
    list of the students that attended the school.
    Precondition:
    The file provided is a student dataset that follows
    the following row pattern:
    School,Age,StudyTime,Failures,Health,Absences,G1,G2,G3
    >>>> student_school_dictionary(student-mat.csv)
    { 'GP' : [ {'Age': 18, 'StudyTime': 1.8, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6 },
    'MB' : ...}
    {another element},
    ...  ],
    [ {'Age': 16, 'StudyTime': 2.6, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 10, 'G2': 12, 'G3': 12 },
    {another element},... ],
    ...}
    """
    student_school_dict = {}
    # Open the file
    in_file = open(file, "r")
    header = in_file.readline()
    header_elements = header.split('\n')[0].split(",")

    # Read the file line by line
    for line in in_file:
        # removes the whitespaces
        # fix to remove \n from the last element
        temp_line = line.split('\n')

        # Split into tokens

        line_elements = temp_line[0].split(",")
        # Expected data sequence
        # line_elements[0]: School
        # line_elements[1]: Age
        # line_elements[2]: StudyTime
        # line_elements[3]: Failures
        # line_elements[4]: Health
        # line_elements[5]: Absences
        # line_elements[6]: G1
        # line_elements[7]: G2
        # line_elements[8]: G3

        # create the value
        temp_dict = {header_elements[1]: int(line_elements[1]),
                     header_elements[2]: int(line_elements[2]),
                     header_elements[3]: int(line_elements[3]),
                     header_elements[4]: int(line_elements[4]),
                     header_elements[5]: int(line_elements[5]),
                     header_elements[6]: int(line_elements[6]),
                     header_elements[7]: int(line_elements[7]),
                     header_elements[8]: int(line_elements[8])}

        # Insert/add into dictionary
        if line_elements[0] in student_school_dict.keys():
            student_school_dict[line_elements[0]].append(temp_dict)
        else:
            student_school_dict[line_elements[0]] = [temp_dict]

    # close the file
    in_file.close()

    return student_school_dict

# ======================================================
# 2


def student_health_dictionary(filename: str) -> List[dict]:
    """
    Returns the keys of the dictionary where the students' health are represented by numbers. 
    A student's health range is from 1 (meaning very bad) to 5 (meaning very good).
    Preconditions: Assuming that the data to be loaded contains no errors. 
    Assuming that the data has the shape of the one provided in student-mat.csv.
    Examples:
    >>>student_health_dictionary("student-mat.csv")
    {1: [{'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Absences': 6, 'G1': 6, 'G2': 5, 'G3': 6},{another element}, ...]...}
    """
    infile = open(filename, "r")
    next(infile)

    student_health = {}
    for i in range(1, 6):
        student_health[(i)] = []
    for line in infile:
        new_list = line.strip('\n').split(',')

        key = int(new_list[4])

        student_list = {'School': new_list[0], 'Age': int(new_list[1]),
                        'StudyTime': int(new_list[2]), 'Failures': int(new_list[3]),
                        'Absences': int(new_list[5]), 'G1': int(new_list[6]),
                        'G2': int(new_list[7]), 'G3': int(new_list[8])}

        student_health[key].append(student_list)

    return student_health


# ======================================================
# 3


def student_age_dictionary(file: str) -> dict:
    """
    Load data from file into program and data will be stored in a dictionary based on age.
    Preconditions: 15 <= age <= 22

    Example:
    >>> { 15 : [ {'School': 'GP', 'StudyTime': 4.2, 'Failures': 3,'Health': 3, 'Absences': 6, 'G1': 7, 'G2': 8, 'G3': 10},{another element},… ],
    16 : [ {'School': 'MS', 'StudyTime': 1, 'Failures': 1.2,'Health': 4, 'Absences': 10, 'G1': 9, 'G2': 11, 'G3': 7},{another element},… ],...}
    """

    in_file = open(file, "r")
    next(in_file)

    student_age = {}

    for i in range(15, 23):
        student_age[(i)] = []

    for line in in_file:
        new_list = line.strip("\n").split(",")

        key = int(new_list[1])

        student_list = {"School": new_list[0],
                        "StudyTime": int(new_list[2]),
                        "Failures": int(new_list[3]),
                        "Health": int(new_list[4]),
                        "Absences": int(new_list[5]),
                        "G1": int(new_list[6]),
                        "G2": int(new_list[7]),
                        "G3": int(new_list[8])}

        student_age[key].append(student_list)

    return student_age

# ======================================================
# 4


def student_failures_dictionary(filename: str) -> dict:
    """
    Returns a dictionary of statistics of student failures, given a filename of a .csv file. The keys of the dictionary are the number of past failures the students have had. 
    Preconditions: Past failures range from 0 to 10

    >>> student_failures_dictionary(student-mat.csv)
    { 0 : [ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 0,     'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14},   {another element},    … ],   1 : [ {'School': 'MS', 'Age': 21, 'StudyTime': 1.8, 'Failures': 2,     'Health': 2, 'Absences': 3, 'G1': 11, 'G2': 11, 'G3': 8},    {another element},    …  ],   … } 
    """
    infile = open(filename, "r")
    main_dict = {}
    mini_dict = {}
    next(infile)
    for line in infile:
        temp_list = line.split("\n")

        temp_list_2 = temp_list[0].split(",")

        mini_dict = {"School": temp_list_2[0],
                     "Age": int(temp_list_2[1]),
                     "StudyTime": int(temp_list_2[2]),
                     "Health": int(temp_list_2[4]),
                     "Absences": int(temp_list_2[5]),
                     "G1": int(temp_list_2[6]),
                     "G2": int(temp_list_2[7]),
                     "G3": int(temp_list_2[8])}

        if temp_list_2[3] in main_dict.keys():
            main_dict[temp_list_2[3]].append(mini_dict)
        else:
            main_dict[temp_list_2[3]] = [mini_dict]
    return main_dict

# ======================================================


def load_data(file_name: str, key: str) -> dict:
    """
    The function lets the user choose how the data will be loaded (i.e., which of the four
    functions you developed should be used).
    It takes two input parameters: (1) the file name where the data is stored, and (2)
    a string describing the key of the dictionary to be returned ('School', 'Age',
    'Health', 'Failures').
    It returns a dictionary with the data loaded using the key based on the input
    parameter. If the key provided is not valid, the function will print the error
    message “Invalid Key” and return an empty dictionary.
    Precondition:
    file_name file should be present in the directory
    key should exist in th dictionary
    >>>load_data("student-mat.csv", "School")
    { 'GP' : [ {'Age': 18, 'StudyTime': 1.8, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6 },
    'MB' : ...}
    {another element},
    ...  ],
    [ {'Age': 16, 'StudyTime': 2.6, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 10, 'G2': 12, 'G3': 12 },
    {another element},... ],
    ...}
    """

    if key == 'School':
        return student_school_dictionary(file_name)
    elif key == 'Age':
        return student_age_dictionary(file_name)
    elif key == 'Health':
        return student_health_dictionary(file_name)
    elif key == 'Failures':
        return student_failures_dictionary(file_name)
    else:
        print("Invalid Key")

# ======================================================


def add_average(dictionary: dict) -> dict:
    """
    Calculates the average grade from the values with keys: G1, G2, G3
    Precondition:
    The dictionary should be correctly formatted 
    >>>add_average(dictionary)
    { 'GP' : [ {'Age': 18, 'StudyTime': 1.8, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67 },
    'MB' :
    ...}
    {another element},
    ...  ],
    [ {'Age': 16, 'StudyTime': 2.6, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 10, 'G2': 12, 'G3': 12, 'G_Avg': 11.33 }, {another element},
    ... ],
    """
    dictionary_copy = dictionary.copy()
    for key, value in dictionary_copy.items():
        for inner_dict in value:
            average = (inner_dict['G1'] +
                       inner_dict['G2'] + inner_dict['G3'] ) / 3
            inner_dict['G_Avg'] = average
    return dictionary_copy

# ======================================================
# Test methods

# 1


def test_dictionary_keys() -> None:
    """
    The function tests the student_school_dictionary, student_health_dictionary,
    student_age_dictionary and student_failures_dictionary functions from the
    T078_M1_load_data modulee.

    Each of the function returns a dictionary and the order of the keys in each
    dictionary is not ensured. Inorder to test the function, we need to test 
    that each key is present in the dictionary returned by the functions.
    Examples
    >>> test_dictionary_keys()
    student_school_dictionary_keys('student-mat.csv') PASSED
    ------
    student_health_dictionary('student-mat.csv') PASSED
    ------
    student_age_dictionary('student-mat.csv') PASSED
    ------
    student_failures_dictionary('student-mat.csv') PASSED
    ------
    Passed: 4/ 4 
    """

    # Define the keys that are expected for each function
    expected_student_school_dictionary_keys = ['GP', 'MB', 'CF', 'BD', 'MS']
    expected_student_health_dictionary_keys = [1, 2, 3, 4, 5]
    expected_student_age_dictionary_keys = [15, 16, 17, 18, 19, 20, 21, 22]
    expected_student_failures_dictionary_keys = ['0', '3', '2', '1']

    # Variablees to store the results of the comparision
    expected_student_school_dictionary_keys_check = False
    expected_student_health_dictionary_keys_check = False
    expected_student_age_dictionary_keys_check = False
    expected_student_failures_dictionary_keys_check = False

    # Variables to keep track of the count of the test cases and the falied ones
    count = 0
    failed_string = ""

    # Checking the student_school_dictionary_keys function
    # store the returned returned
    returned_dict_keys = student_school_dictionary(
        ('student-mat.csv')).keys()

    expected_student_school_dictionary_keys_check = check_keys_unordered(returned_dict_keys,
                                                                         expected_student_school_dictionary_keys)
    check_equal('student_school_dictionary_keys(\'student-mat.csv\')',
                expected_student_school_dictionary_keys_check,
                True)

    if expected_student_school_dictionary_keys_check == True:
        count += 1
    else:
        failed_string += 'student_school_dictionary_keys\n'

    returned_dict_keys = student_health_dictionary(
        ('student-mat.csv')).keys()

    expected_student_health_dictionary_keys_check = check_keys_unordered(returned_dict_keys,
                                                                         expected_student_health_dictionary_keys)

    check_equal('student_health_dictionary(\'student-mat.csv\')',
                expected_student_health_dictionary_keys_check,
                True)

    if expected_student_health_dictionary_keys_check == True:
        count += 1
    else:
        failed_string += 'student_health_dictionary\n'

    returned_dict_keys = student_age_dictionary(
        ('student-mat.csv')).keys()

    expected_student_age_dictionary_keys_check = check_keys_unordered(returned_dict_keys,
                                                                      expected_student_age_dictionary_keys)

    check_equal('student_age_dictionary(\'student-mat.csv\')',
                expected_student_age_dictionary_keys_check,
                True)

    if expected_student_age_dictionary_keys_check == True:
        count += 1
    else:
        failed_string += 'student_age_dictionary\n'

    returned_dict_keys = student_failures_dictionary(
        ('student-mat.csv')).keys()

    expected_student_failures_dictionary_keys_check = check_keys_unordered(returned_dict_keys,
                                                                           expected_student_failures_dictionary_keys)

    check_equal('student_failures_dictionary(\'student-mat.csv\')',
                expected_student_failures_dictionary_keys_check,
                True)

    if expected_student_failures_dictionary_keys_check == True:
        count += 1
    else:
        failed_string += 'student_failures_dictionary\n'

    if(count == 4):
        print("Passed: {0}/ 4 ".
              format(count))
    else:
        print("Passed: {0}/ 4, \nfailed functions: \n{1} ".
              format(count, failed_string))


def check_keys_unordered(actual_keys: list, expected_keys: list) -> bool:
    """
    The function checks that each element in actual_keys list is the present
    in the expected_keys once assuming that the order doesnot matter.
    Precondition: None
    Examples:
    >>> check_keys_unordered([], [])
    True
    >>> check_keys_unordered([1,1], [1,1])
    True
    >>> check_keys_unordered([1], [1,1])
    Length of the keys list are not equal, Actual:  [1]  Expected:  [1, 1]
    False
    >>> check_keys_unordered([2], [3])
    Key 3  is not in: Actual list [2]  Expected list:  [3]
    False
    """
    if len(actual_keys) != len(expected_keys):
        print("Length of the keys list are not equal, Actual: ",
              actual_keys, " Expected: ", expected_keys)
        return False

    for key in expected_keys:
        # print("key is: ", key)
        if (key not in actual_keys):
            print("Key", key, " is not in: Actual list", actual_keys,
                  " Expected list: ", expected_keys)
            return False

    return True


# ======================================================
# 2
def test_length_equal() -> None:
    """
    The function tests the student_school_dictionary, student_health_dictionary,
    student_age_dictionary and student_failures_dictionary functions from the
    T078_M1_load_data modulee. Prints a "passed" message if actual and expected 
    have same type and are equal (as determined by the == operator); otherwise,
    print a "fail" message.
    Preconditions: Expects no user input
    Example:
    >>>test_length_equal()
    student_school_dictionary PASSED
    ------
    student_health_dictionary PASSED
    ------
    student_age_dictionary PASSED
    ------
    student_failures_dictionary PASSED
    ------
    Passed 4 out of 4 tests
    Failed 0 out of 4 tests
    """
    test_passed = 0
    test_failed = 0
    test_done = 0
    check_equal("student_school_dictionary", check_size_equal(
        student_school_dictionary("student-mat.csv"), "student-mat.csv"), True)
    if check_size_equal(student_school_dictionary("student-mat.csv"), "student-mat.csv") == True:
        test_passed += 1
    else:
        test_failed += 1
    test_done += 1
    check_equal("student_health_dictionary", check_size_equal(
        student_health_dictionary("student-mat.csv"), "student-mat.csv"), True)
    if check_size_equal(student_school_dictionary("student-mat.csv"), "student-mat.csv") == True:
        test_passed += 1
    else:
        test_failed += 1
    test_done += 1
    check_equal("student_age_dictionary", check_size_equal(
        student_age_dictionary("student-mat.csv"), "student-mat.csv"), True)
    if check_size_equal(student_school_dictionary("student-mat.csv"), "student-mat.csv") == True:
        test_passed += 1
    else:
        test_failed += 1
    test_done += 1
    check_equal("student_failures_dictionary", check_size_equal(
        student_failures_dictionary("student-mat.csv"), "student-mat.csv"), True)
    if check_size_equal(student_school_dictionary("student-mat.csv"), "student-mat.csv") == True:
        test_passed += 1
    else:
        test_failed += 1
    test_done += 1
    print("Passed", test_passed, "out of", test_done,
          "tests" "\nFailed", test_failed, "out of", test_done, "tests")


def check_size_equal(actual: dict, expected: str) -> str:
    """
    Returns a bool of type 'True' if actual size of the list and expected size of the list are same.
    Otherwise, returns a bool of type 'False'

    Preconditions: Parameters "actual" and "expected" are the actual value returned
    by a function call expression and the value we expect a correct implementation
    of the function to return, respectively. Both parameters must have the same
    type, which must be a type for which == is used to determine if two values
    are equal.
    Example:
    >>>check_size_equal(student_school_dictionary("student-mat.csv"), "student-mat.csv")
        True
    >>>check_size_equal(student_age_dictionary("student-mat.csv"), "student-mat.csv")
        True
    """
    count = 0
    for x in actual:
        if isinstance(actual[x], list):
            count += len(actual[x])
    rowcount = 0
    # iterating through the whole file
    for row in open(expected):
        rowcount += 1
    # The first row is the header, therefore it is not to be included.
    rowcount -= 1
    actual_value = 0
    test_completed = 0
    test_passed = 0

    if count == rowcount:
        actual_value = True
    else:
        actual_value = False
    return actual_value

# ======================================================
# 3


def test_individual_student_entries() -> None:
    """
    Test ensures that each individual student entries in the dictionaries are stored correctly. 
    """
    count = 0
    failed_list = ""

    student_school_dictionary_keys = ["GP", "MB", "CF", "BD", "MS"]
    student_health_dictionary_keys = [1, 2, 3, 4, 5]
    student_age_dictionary_keys = [15, 16, 17, 18, 19, 20, 21, 22]
    student_failures_dictionary_keys = ['0', '1', '2', '3']

    expected_student_school_dictionary = [
        "Age", "StudyTime", "Failures", "Health", "Absences", "G1", "G2", "G3"]
    expected_student_health_dictionary = [
        "School", "Age", "StudyTime", "Failures", "Absences", "G1", "G2", "G3"]
    expected_student_age_dictionary = [
        "School", "StudyTime", "Failures", "Health", "Absences", "G1", "G2", "G3"]
    expected_student_failures_dictionary = [
        "School", "Age", "StudyTime", "Health", "Absences", "G1", "G2", "G3"]

    file = "student-mat.csv"
    actual_student_school_dictionary = student_school_dictionary(file)
    actual_student_health_dictionary = student_health_dictionary(file)
    actual_student_age_dictionary = student_age_dictionary(file)
    actual_student_failures_dictionary = student_failures_dictionary(file)

    expected_student_school_dictionary_keys = "passed"
    count += 1
    for entry in student_school_dictionary_keys:
        entrys = actual_student_school_dictionary.get(entry)
        for element in entrys:
            element.keys()
            if len(element.keys()) != len(expected_student_school_dictionary):
                expected_student_school_dictionary_keys = "failed"
                failed_list += 'student_school_dictionary_keys\n'
            else:
                for key in expected_student_school_dictionary:
                    if key not in element.keys():
                        failed_list += 'student_school_dictionary_keys\n'
                        expected_student_school_dictionary_keys = "failed"
                        break

    expected_student_health_dictionary_keys = "passed"
    count += 1
    for entry in student_health_dictionary_keys:
        entrys = actual_student_health_dictionary.get(entry)
        for element in entrys:
            element.keys()
            if len(element.keys()) != len(expected_student_health_dictionary):
                expected_student_health_dictionary_keys = "failed"
                failed_list += "student_health_dictionary_keys\n"
            else:
                for key in expected_student_health_dictionary:
                    if key not in element.keys():
                        failed_list += "student_health_dictionary_keys\n"
                        expected_student_health_dictionary_keys = "failed"
                        break

    expected_student_age_dictionary_keys = "passed"
    count += 1
    for entry in student_age_dictionary_keys:
        entrys = actual_student_age_dictionary.get(entry)
        for element in entrys:
            element.keys()
            if len(element.keys()) != len(expected_student_age_dictionary):
                expected_student_age_dictionary_keys = "failed"
                failed_list += "student_age_dictionary_keys\n"
            else:
                for key in expected_student_age_dictionary:
                    if key not in element.keys():
                        failed_list += "student_age_dictionary_keys\n"
                        expected_student_age_dictionary_keys = "failed"
                        break

    expected_student_failures_dictionary_keys = "passed"
    count += 1
    for entry in student_failures_dictionary_keys:
        entrys = actual_student_failures_dictionary.get(entry)
        for element in entrys:
            element.keys()
            if len(element.keys()) != len(expected_student_failures_dictionary):
                expected_student_failures_dictionary_keys = "failed"
                failed_list += "student_failures_dictionary_keys\n"
            else:
                for key in expected_student_failures_dictionary:
                    if key not in element.keys():
                        failed_list += "student_failures_dictionary_keys\n"
                        expected_student_failures_dictionary_keys = "failed"
                        break

    check_equal("student_school_dictionary",
                expected_student_school_dictionary_keys, "passed")

    check_equal("student_health_dictionary",
                expected_student_health_dictionary_keys, "passed")

    check_equal("student_age_dictionary",
                expected_student_age_dictionary_keys, "passed")

    check_equal("student_failures_dictionary",
                expected_student_failures_dictionary_keys, "passed")

    print("Number of tests:", count + len(failed_list))
    print("Tests passed:", count)
    print("Tests failed:", len(failed_list))

# ======================================================
# 4


def test_add_average() -> None:
    """ Tests pass if the arguements placed in the function comparison_check return True (therefore, all three subtests would pass). 

    Parameters: None
    """
    tests_passed_count = 0
    tests_failed = 0
    passed = False

    returned_val = comparison_check("student_school_dictionary(\"student-mat.csv\")", student_school_dictionary(
        "student-mat.csv"), add_average(student_school_dictionary("student-mat.csv")), passed)

    if returned_val == True:
        tests_passed_count += 1
        passed = False
    else:
        tests_failed += 1

    returned_val = comparison_check("student_health_dictionary(\"student-mat.csv\")", student_health_dictionary(
        "student-mat.csv"), add_average(student_health_dictionary("student-mat.csv")), passed)

    if returned_val == True:
        tests_passed_count += 1
        passed = False
    else:
        tests_failed += 1

    returned_val = comparison_check("student_age_dictionary(\"student-mat.csv\")", student_age_dictionary(
        "student-mat.csv"), add_average(student_age_dictionary("student-mat.csv")), passed)

    if returned_val == True:
        tests_passed_count += 1
        passed = False
    else:
        tests_failed += 1

    returned_val = comparison_check("student_failures_dictionary(\"student-mat.csv\")", student_failures_dictionary(
        "student-mat.csv"), add_average(student_failures_dictionary("student-mat.csv")), passed)

    if returned_val == True:
        tests_passed_count += 1
        passed = False
    else:
        tests_failed += 1

    print(tests_passed_count, "/4 ",
          "tests passed when test_add_average is called.", sep="")
    print("Number of tests failed when test_add_average is called: ",
          tests_failed, sep="")


def comparison_check(description: str, actual: dict, expected: dict, test_passed: bool) -> bool:
    """ Returns bool value True if all three subtests are evaluate to True. Prints result of if all three subtests are passed. Subtest 1, the number of students in the dictionary does not change. Subtest 2, the G_Avg key is added to the student dictionary. Subtest 3, the value for G_Avg is properly calculated. Given the folllowing parameters: description, the dictionary before add_average function is called, and the dictionary when add_average function is called.

    Parameters: type(description) is type str, type(actual) is type dict, type(expected) is type dict.
    """
    actual_count = 0
    expected_count = 0
    condition_one = False
    condition_two = False
    condition_three = False
    before_avg = False
    after_avg = False
    conditions = False  # must equal True to pass test
    test_passed = True
    # Check if the number of students in the dictionary does not change

    for i in actual:
        for dict_act in actual[i]:
            actual_count += 1

    for a in expected:
        for dict_exp in expected[a]:
            expected_count += 1

    if actual_count == expected_count:
        condition_one = True
        for dict in expected[i]:

            if 'G_Avg' in dict:
                condition_two = True
            else:
                condition_two = False
    else:
        condition_two = None
        # Check if G_Avg key is added to the student dictionary
        for dict in expected[i]:

            if 'G_Avg' in dict:
                condition_two = True
            else:
                condition_two = False
    print("When add_average is called on ", description, sep="")
    print("[1] The number of students does not change: ", condition_one, sep="")
    print("[2] The G_Avg key is added to the student dictionary: ",
          condition_two, sep="")

    # Check if the value for G_Avg is properly calculated

    for key, value in expected.items():
        for inner_dict in value:
            average = (inner_dict['G1'] +
                       inner_dict['G2'] + inner_dict['G3'] ) / 3
            #inner_dict['G_Avg'] = average
            sample_variable = inner_dict.get("G_Avg")

            if sample_variable == average:
                condition_three = True
            else:
                condition_three = False

    print("[3] The value for G_Avg is properly calculated: ",
          condition_three, sep="")
    # Print the results. Do the tests pass or fail.
    if condition_one == condition_two == condition_three == True:
        before_avg = True
        after_avg = True
        check_equal(description, before_avg, after_avg)
        return test_passed
    else:
        before_avg = False
        after_avg = True
        check_equal(description, before_avg, after_avg)


# main function
if __name__ == "__main__":

    test_dictionary_keys()

    test_individual_student_entries()

    test_length_equal()

    test_add_average()
