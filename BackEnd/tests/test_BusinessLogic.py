""""

    Author: Thomas Theis, 2021

"""


import os
import sys

# Make sure that the application source directory (this directory's parent) is
# on sys.path.

here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, here)

from BusinessLogic import BusinessLogic as BL

bl = BL('./restaurants.csv')

def test_BL_epoch_of_string_working():
    try:
        t = bl.epoch_of_string("2021:06:30:16:30")
        assert(t == 1625085000.0)
    except Exception:
        assert(False)


def test_BL_epoch_of_string_not_working_seconds():
    try:
        t = bl.epoch_of_string("2021:06:30:16:30:01")
        assert(False)
    except ValueError:
        assert(True)
    except Exception:
        assert(False)

def test_BL_epoch_of_string_not_working_missing_time():
    try:
        t = bl.epoch_of_string("30:16:30")
        assert(False)
    except ValueError:
        assert(True)
    except Exception:
        assert(False)

def test_BL_epoch_of_string_not_working_text():
    try:
        t = bl.epoch_of_string("fish")
        assert(False)
    except ValueError:
        assert(True)
    except Exception:
        assert(False)

def test_BL_justify_string_working1():
    try:
        t = bl.justify_string("2021:06:30:16:30")
        assert(True)
    except ValueError:
        assert(False)
    except Exception:
        assert(False)

def test_BL_justify_string_working2():
    try:
        t = bl.justify_string("06:30:16:30")
        assert(True)
    except ValueError:
        assert(False)
    except Exception:
        assert(False)

def test_BL_justify_string_working3():
    try:
        t = bl.justify_string("30:16:30")
        assert(True)
    except ValueError:
        assert(False)
    except Exception:
        assert(False)

def test_BL_justify_string_working4():
    try:
        t = bl.justify_string("16:30")
        assert(True)
    except ValueError:
        assert(False)
    except Exception:
        assert(False)

def test_BL_justify_string_working5():
    try:
        t = bl.justify_string("30")
        assert(True)
    except ValueError:
        assert(False)
    except Exception:
        assert(False)

def test_BL_justify_string_incorrect_length_too_long():
    try:
        t = bl.justify_string("2021:06:30:16:30:01")
        assert(False)
    except ValueError:
        assert(True)
    except Exception:
        assert(False)

def test_BL_justify_string_incorrect_length_too_short():
    try:
        t = bl.justify_string("2021:06:30:16")
        assert(False)
    except ValueError:
        assert(True)
    except Exception:
        assert(False)

def test_BL_justify_string_incorrect_month():
    try:
        t = bl.justify_string("2021:30:16:30")
        assert(False)
    except ValueError:
        assert(True)
    except Exception:
        assert(False)

def test_BL_justify_string_incorrect_digit():
    try:
        t = bl.justify_string("2021:O6:30:16:30")
        assert(False)
    except ValueError:
        assert(True)
    except Exception:
        assert(False)

def test_BL_get_day_of_week():
    try:
        t = bl.get_day_of_week("2021:06:30:16:30")
        assert(t == "Wednesday")
    except ValueError:
        assert(False)
    except Exception:
        assert(False)

def test_BL_get_day_of_passover():
    try:
        t = bl.get_day_of_week("2020:02:29:16:30")
        assert(t == "Saturday")
    except ValueError:
        assert(False)
    except Exception:
        assert(False)