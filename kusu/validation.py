"""__author__ = Kieran Wood

Description:
    A set of utilities for validating input

Testing:
    Run the file directly from terminal $ python3 kusu/validation.py

TODO:
    * Add extension validation function
"""


def validate_int_selection(maximum = 1, minimum=0, message = "Please select a number between 0 and 1: "):
        """Validates entry is an int and is between the minimum and maximum

        Args:
            maximum (int): The maximum value (inclusive)
            minimum (int): The minimum value (inclusive)
            Message (str): What to prompt user with when function is called
        """
        valid_answer = False

        while valid_answer == False:
            try: # Catches if answer is not int or float
                selection = eval(input(message))
            except:
                print("Invalid input please try again")

            if selection > maximum: # More than maximum
                print("Invalid input the selection made was larger than {}".format(maximum))

            elif selection < minimum:#Less than minimum
                print("Invalid input the selection made was smaller than {}".format(minimum))

            else: # If answer is valid and in range
                return selection

def validate_extension():
    """Validates and/or modifies string to check/set correct extension
    """
    pass

if __name__ == "__main__":
    validate_int_selection()