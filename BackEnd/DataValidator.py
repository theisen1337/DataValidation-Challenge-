""""

    Author: Thomas Theis, 2021
    This class is used for Validating data, standardizing data.
    Following PEP8 Style Guide https://www.python.org/dev/peps/pep-0008/

"""

# Part of standard Python 3.8
import csv
import os
import re
import copy

# SelfMade
from Utility import Utility as util

DayKey = {
    'Mon': 0,
    'Tues': 1,
    'Wed': 2,
    'Thu': 3,
    'Fri': 4,
    'Sat': 5,
    'Sun': 6,
}

DayStandard = {
    'Mon': 'Monday',
    'Tues': 'Tuesday',
    'Wed': 'Wednesday',
    'Thu': 'Thursday',
    'Fri': 'Friday',
    'Sat': 'Saturday',
    'Sun': 'Sunday',
}


class DataValidator(object):

    def __init__(self):
        self.header = ""
        super(DataValidator, self).__init__()

    def _to_military_time(self, time_str: str) -> int:
        """
        :param time_str: String that contains time.
        :return int: Integer of time in Military time.

            This is a private function that should be only called from within this class, and test.
            This will attempt to covert time to Military time.

            Examples:
                1:00 am      -> 100
                11:40 Am  -> 1140
                12:00 PM     -> 1200
                12:00 aM  -> 0

        """

        # Must be in correct format
        time_str = self._standard_time_format(time_str)

        # Check for AM, or PM
        if 'AM' in str(time_str).upper():

            time_int = util.string_to_int(time_str)

            # 12:00 AM - 12:59 AM
            if time_int >= 1200:
                return time_int - 1200
            else:
                return time_int

        elif 'PM' in str(time_str).upper():
            time_int = util.string_to_int(time_str)

            # 12:00 PM to 12:59 PM
            if time_int >= 1200:
                return time_int
            else:
                return util.string_to_int(time_str) + 1200
        else:
            print("No Implementation for time that is not AM/am or PM/pm", time_str)
            raise NotImplementedError

    @staticmethod
    def _standard_time_format(time_str: str) -> str:
        """
        :param time_str: string that has time
        :return: standardized string of time

            This is a private function that should be only called from within this class, and test.
            This will attempt to covert 2 digit time to 4 digit format time.

            Examples:
                1 am -> 1:00 am
                1 Pm -> 1:00 Pm
                7 pM -> 7:00 pM
                8:00 am -> 8:00 am

        """

        if len(util.string_to_int_str(time_str)) <= 4 and ':' in time_str:
            # 00:01 - 00:59
            # 12:00, 1:59

            # Try to validate input data
            if util.string_to_int(time_str) > 1259 or \
                util.string_to_int(time_str) < 1 or \
                    ('AM' not in time_str.upper() and 'PM' not in time_str.upper()):
                print("Error with value: ", time_str, " looking for values like 11:00 am, 7:00 pm, 3:15 am")
                raise ValueError

            return time_str

        elif len(util.string_to_int_str(time_str)) <= 2:
            # 12 pm
            # 2 am

            # Try to validate input data
            if util.string_to_int(time_str) > 12 or \
                    util.string_to_int(time_str) < 1 or \
                    ('AM' not in time_str.upper() and 'PM' not in time_str.upper()):
                print('Error with value: ', time_str, " looking for values like 11 am, 7 pm, 3:15 am")
                raise ValueError

            return str(util.string_to_int_str(time_str) + ":00" + time_str.split(" ")[1])
        else:
            print("No Implementation for time that is not 00:00 or 00 ", time_str)
            raise ValueError

    def _parse_time_chunk(self, chunk: str) -> dict:
        """
        :param chunk: Is a string that holds the days and hours
        :return: dictionary that is standardized.

            This is a private function that should be only called from within this class, and test.
            {
                "day": [MilitaryTime Open, MilitaryTime Close],
                "Monday": [900, 1700]
            }

        """

        time_standard = {}

        midpoint = util.first_digit_index(chunk)
        days = chunk[:midpoint]
        hours = chunk[midpoint:]

        # parse Days
        for d in list(filter(None, list(re.split('[, ]', days)))):

            if '-' in d:
                # Range of Days.
                first, last = d.split('-')

                # Check that days are valid
                if first not in list(DayKey.keys()) or last not in list(DayKey.keys()):
                    print("Found Invalidate days in: ", days, " >>>", first, " - ", last)
                    raise ValueError

                # grab range.
                time_standard[DayStandard[first]] = []
                while first != last:
                    # Iterate begin_sub_chunk until it is equal end_sub_chunk
                    first = util.key_by_index(DayKey, (DayKey[first] + 1) % len(list(DayKey.keys())))

                    # Set Standardized time using DayStandard dict
                    time_standard[DayStandard[first]] = []

            else:
                # Single day.
                # Check that day is valid
                if d not in list(DayKey.keys()):
                    print("Found Invalidate day in: ", days, " >>>", d)
                    raise ValueError

                #
                time_standard[DayStandard[d]] = []

        # parse Hours
        open_time, close_time = hours.split(' - ')

        open_time = self._standard_time_format(open_time)
        open_time = self._to_military_time(open_time)
        close_time = self._standard_time_format(close_time)
        close_time = self._to_military_time(close_time)

        for k in list(time_standard.keys()):
            time_standard[k].extend([open_time, close_time])

        return copy.deepcopy(time_standard)

    def _validation(self, data: list) -> dict:
        """
        :param data: Is list of tuples that is brought in from CSV
        :return dict: Standardized Dictionary that all business logic will use.

            This is a private function that should be only called from within this class, and test.
            This will attempt to validate and standardize data.

            Known data rules:

            1. First entry can contain numbers or text.         -> Parse first entry to str()
            2. Time starts with a day chunk. i.e. "Day," or "Day-Day"
            3. Day must be inside of global "DayKey"            -> Throw ValueError if not.


            Example of return:
                {
                    'Restaurant Name': {
                                            'day': [MilitaryTime Open, MilitaryTime Close],
                                            'Monday': [900, 1700]
                                        },
                    'Bida Manda': {
                                    'Monday': [1130, 2200],
                                    'Tuesday': [1130, 2200],
                                    'Wednesday': [1130, 2200],
                                    'Thursday': [1130, 2200],
                                    'Sunday': [1130, 2200],
                                    'Friday': [1130, 2300],
                                    'Saturday': [1130, 2300]}
                                  },
                }

            Rule for data, a opening time, and a closing time that are the same i.e. 'Sunday': [0, 0] is closed
            for the day.

        """

        # Go through and validate and standardize data structure.
        dict_data = {}
        for i in data:
            if str(i[0]) in list(dict_data.keys()):
                print("Found duplication of restaurant")
                raise ValueError
            else:
                # Standardize data
                name = str(i[0])
                time = str(i[1])

                time_standardized = {}

                # Check to see if there are multiple chunks.
                if '/' in time:
                    for chunk in time.split("/"):
                        # Concat dictionaries
                        time_standardized = {**time_standardized, **self._parse_time_chunk(chunk)}

                else:
                    time_standardized = self._parse_time_chunk(time)

                # Setup return dictionary with name, and time
                dict_data[name] = time_standardized

        return copy.deepcopy(dict_data)

    def open_file(self, input_file: str) -> dict:
        """
        :param input_file:
        :return list:

            This will handle validation of the data, and will fail on malformed data.

            Example of return:
                {
                    'Restaurant Name': {
                                            'day': [MilitaryTime Open, MilitaryTime Close],
                                            'Monday': [900, 1700]
                                        },
                    'Bida Manda': {
                                    'Monday': [1130, 2200],
                                    'Tuesday': [1130, 2200],
                                    'Wednesday': [1130, 2200],
                                    'Thursday': [1130, 2200],
                                    'Sunday': [1130, 2200],
                                    'Friday': [1130, 2300],
                                    'Saturday': [1130, 2300]}
                                  },
                }

            Rule for data, a opening time, and a closing time that are the same i.e. 'Sunday': [0, 0] is closed
            for the day.

        """

        # Check that file exist
        if not os.path.exists(input_file):
            print("Path does not exist:", input_file)
            raise FileNotFoundError

        # Container to hold data for the time being
        read_data = []

        # Open csv file for reading
        with open(input_file, "r") as file:
            # Parse csv data
            parsed = csv.reader(file, delimiter=',', lineterminator='\r\n', quotechar='"')

            row_counter = 0
            for row in parsed:
                # Check if row is header.
                if row_counter == 0:
                    self.header = row
                else:
                    read_data.append(row)

                # increment counter
                row_counter += 1

        # Try to do Validation on data.
        return self._validation(read_data)


if __name__ == "__main__":
    DV = DataValidator()
    DV.open_file('../restaurants.csv')
