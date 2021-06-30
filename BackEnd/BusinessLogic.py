""""

    Author: Thomas Theis, 2021
    This class is used for the actual business logic
    Following PEP8 Style Guide https://www.python.org/dev/peps/pep-0008/

"""
# Python Standard Libraries
import datetime

# SelfMade
from DataValidator import DataValidator as dV
from Utility import Utility as uTil


class BusinessLogic (object):

    def __init__(self, file_path: str):
        dv = dV()
        self.dv = dv
        self.restaurants = dv.open_file(file_path)
        super(BusinessLogic, self).__init__()

    @staticmethod
    def current_epoch() -> float:
        """
        :return: float of the number of seconds since epoch with precision e5
        """
        return datetime.datetime.now().timestamp()

    @staticmethod
    def current_date() -> str:
        """
        :return: Date String in the format YYYY:MM:DD:HH:MM of current time.
        """
        return datetime.datetime.now().strftime('%Y:%m:%d:%H:%M')

    @staticmethod
    def epoch_of_string(time_str: str) -> float:
        """
        :param time_str: Exspecting string of format YYYY:MM:DD:HH:MM
        :return:
        """
        # Try catch blocks are slow, but sometimes it is the best validation
        try:
            timestamp = datetime.datetime.strptime(time_str, '%Y:%m:%d:%H:%M').timestamp()
            return timestamp
        except Exception as e:
            raise e

    @staticmethod
    def justify_string(time_str: str) -> str:
        """
        :param time_str: string of time
        :return: correct format YYYY:MM:DD:HH:MM

            Takes a string of:
                YYYY:MM:DD:HH:MM    ->   YYYY:MM:DD:HH:MM
                     MM:DD:HH:MM    ->   YYYY:MM:DD:HH:MM
                        DD:HH:MM    ->   YYYY:MM:DD:HH:MM
                           HH:MM    ->   YYYY:MM:DD:HH:MM
                              MM    ->   YYYY:MM:DD:HH:MM

            All empty missing segments will be filled with current time.
        """
        # Grab current time.
        current = datetime.datetime.now().strftime('%Y:%m:%d:%H:%M')
        current_list = list(str(current).split(':'))
        time_list = list(time_str.split(':'))

        # Cut end of current list to make room for
        current_list = current_list[:len(current_list) - len(time_list)]
        current_list.extend(time_list)

        # Add time_list to end of current_list
        time_list = ':'.join(current_list)

        # Attempt to Validate Time
        try:
            datetime.datetime.strptime(time_list, '%Y:%m:%d:%H:%M')
            return str(time_list)
        except Exception:
            raise ValueError

    def get_restaurants(self) -> dict:
        """
        :return: return data structure of restaurants
        """
        return self.restaurants

    def get_day_of_week(self, time_str: str) -> str:
        """
        :param time_str: string time expecting format YYYY:MM:DD:HH:MM
        :return: Day of the Week i.e. Monday, Tuesday, etc.
        """
        # Try to justify time.
        time_str = self.justify_string(time_str)

        # Get index of day
        day_index = datetime.datetime.strptime(time_str, '%Y:%m:%d:%H:%M').weekday()

        # Get Shorthand of the day.
        day_short = uTil.key_by_index(self.dv.get_day_key(), day_index)

        # return full day standardized
        return self.dv.get_day_standard()[day_short]

    def get_open_restaurants(self, time_str: str) -> list:
        """
        :param time_str: Takes string of format YYYY:MM:DD:HH:MM
        :return: list of open restaurants.

            Will look into list of restaurants and grab all the ones currently open.

        """
        time_str = self.justify_string(time_str)
        day = self.get_day_of_week(time_str)

        # Time to standard that DataValidator can handle it.
        hour = uTil.string_to_int(time_str.split(':')[-2])
        minute = uTil.string_to_int(time_str.split(':')[-1])

        if hour > 12:
            new_time_str = str(str(hour - 12) + ":" + str(minute) + " pm")
        else:
            new_time_str = str(str(hour) + ":" + str(minute) + " am")

        # To military time
        mil_time = self.dv.to_military_time(new_time_str)

        open_restaurants = []
        restaurants = self.get_restaurants()
        for k in list(restaurants.keys()):
            for k2 in list(restaurants[k].keys()):

                if day == k2:
                    if restaurants[k][k2][0] == restaurants[k][k2][1]:
                        # Restaurant closed this day.
                        pass
                    elif (restaurants[k][k2][0] <= mil_time) and (restaurants[k][k2][1] >= mil_time):
                        # Restaurant currently open.
                        open_restaurants.append(k)
        return open_restaurants
