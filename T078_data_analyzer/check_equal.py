# Arif Aziz, Tanner Farkas , Meagan Pitts, Jason Dmello
''' A unit testing framework for ECOR1042 '''


def check_equal(description: str, actual, expected) -> None:
    """
    Print a "passed" message if actual and expected are equal 
    (as determined by the == operator); otherwise, print a 
    "fail" message.

    Parameter "description" should provide information that will help us
    interpret the test results; e.g., the call expression that yields
    actual.

    Parameters "actual" and "expected" are typically the actual value returned
    by a call expression and the value we expect a correct implementation
    of the function to return, respectively. Both parameters must have the same
    type, which must be a type for which == is used to determine if two values
    are equal. Don't use this function to check if floats, lists of floats,
    tuples of floats, etc. are equal. 
    """
    if actual != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, actual))
    else:
        print("{0} PASSED".format(description))
    print("------")
