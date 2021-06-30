""""

    Author: Thomas Theis, 2021
    This class is used for general utilities.
    Following PEP8 Style Guide https://www.python.org/dev/peps/pep-0008/

"""

class Utility(object):

    @classmethod
    def key_by_index(cls, my_dict: dict, value: object) -> str:
        """
        :param my_dict: Pass in dictoinary
        :param value: Pass in lookup value
        :return str:

            Helper function to return FIRST key, by the value.

        """
        tmp = list(my_dict.keys())[list(my_dict.values()).index(value)]

        # check if there is one item or more.
        if isinstance(tmp, str):
            return tmp
        else:
            return tmp[0]

    @staticmethod
    def has_digit(line: str) -> bool:
        """
        :param line: String
        :return bool: boolean if sting contains any numbers or not.

            Helper Function to return True/False any digit in string.
        """
        return len([x for x in range(0, len(line)) if line[x].isdigit()]) > 0

    @classmethod
    def first_digit_index(cls, line: str) -> int:
        """
        :param line: String containing digits
        :return int: index of first number

            Helper Function to return first index of a digit in a string
        """
        if not cls.has_digit(line):
            raise ValueError

        return [x for x in range(0, len(line)) if line[x].isdigit()][0]

    @classmethod
    def string_to_int_str(cls, line: str) -> str:
        """
        :param line: a string with digits
        :return str: all digits collapsed into one number

            Helper function for combing all characters that represent a digit,
            into a single number str.

        """
        if not cls.has_digit(line):
            raise ValueError

        return str(''.join(filter(str.isdigit, line)))

    @classmethod
    def string_to_int(cls, line: str) -> int:
        """
        :param line: a string with digits
        :return int: all digits collapsed into one number

            Helper function for combing all characters that represent a digit,
            into a single number and converting it into a int().

        """
        if not cls.has_digit(line):
            raise ValueError

        return int(''.join(filter(str.isdigit, line)))
