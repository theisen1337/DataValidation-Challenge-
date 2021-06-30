""""

    Author: Thomas Theis, 2021

"""


import sys, os

# Make sure that the application source directory (this directory's parent) is
# on sys.path.

here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, here)


import DataValidator as dv


test_data =[
    ["The Cowfish Sushi Burger Bar", "Mon-Sun 11:00 am - 10 pm"],
    ["Morgan St Food Hall", "Mon-Sun 11 am - 9:30 pm"],
    ["Beasley's Chicken + Honey", "Mon-Fri, Sat 11 am - 12 pm / Sun 11 am - 10 pm"],
    ["Garland", "Tues-Fri, Sun 11:30 am - 10 pm / Sat 5:30 pm - 11 pm"],
    ["Crawford and Son", "Mon-Sun 11:30 am - 10 pm"],
    ["Death and Taxes", "Mon-Sun 5 pm - 10 pm"],
    ["Caffe Luna", "Mon-Sun 11 am - 12 am"],
    ["Bida Manda", "Mon-Thu, Sun 11:30 am - 10 pm / Fri-Sat 11:30 am - 11 pm"],
    ["The Cheesecake Factory", "Mon-Thu 11 am - 11 pm / Fri-Sat 11 am - 12:30 am / Sun 10 am - 11 pm"],
    ["Tupelo Honey", "Mon-Thu, Sun 9 am - 10 pm / Fri-Sat 9 am - 11 pm"],
    ["Player's Retreat", "Mon-Thu, Sun 11:30 am - 9:30 pm / Fri-Sat 11:30 am - 10 pm"],
    ["Glenwood Grill", "Mon-Sat 11 am - 11 pm / Sun 11 am - 10 pm"],
    ["Neomonde", "Mon-Thu 11:30 am - 10 pm / Fri-Sun 11:30 am - 11 pm"],
    ["Page Road Grill", "Mon-Sun 11 am - 11 pm"],
    ["Mez Mexican", "Mon-Fri 10:30 am - 9:30 pm / Sat-Sun 10 am - 9:30 pm"],
    ["Saltbox", "Mon-Sun 11:30 am - 10:30 pm"],
    ["El Rodeo", "Mon-Sun 11 am - 10:30 pm"],
    ["Provence", "Mon-Thu, Sun 11:30 am - 9 pm / Fri-Sat 11:30 am - 10 pm"],
    ["Bonchon", "Mon-Wed 5 pm - 12:30 am / Thu-Fri 5 pm - 1:30 am / Sat 3 pm - 1:30 am / Sun 3 pm - 11:30 pm"],
    ["Tazza Kitchen", "Mon-Sun 11 am - 10 pm"],
    ["Mandolin", "Mon-Thu 11 am - 10 pm / Fri-Sat 10 am - 10:30 pm / Sun 11 am - 11 pm"],
    ["Mami Nora's", "Mon-Sat 11 am - 10 pm / Sun 12 pm - 10 pm"],
    ["Gravy", "Mon-Sun 11 am - 10 pm"],
    ["Taverna Agora", "Mon-Thu, Sun 11 am - 10 pm / Fri-Sat 11 am - 12 am"],
    ["Char Grill", "Mon-Fri 11:30 am - 10 pm / Sat-Sun 7 am - 3 pm"],
    ["Seoul 116", "Mon-Sun 11 am - 4 am"],
    ["Whiskey Kitchen", "Mon-Thu, Sun 11:30 am - 10 pm / Fri-Sat 11:30 am - 11 pm"],
    ["Sitti", "Mon-Sun 11:30 am - 9:30 pm"],
    ["Stanbury", "Mon-Sun 11 am - 12 am"],
    ["Yard House", "Mon-Sun 11:30 am - 10 pm"],
    ["David's Dumpling", "Mon-Sat 11:30 am - 10 pm / Sun 5:30 pm - 10 pm"],
    ["Gringo a Gogo", "Mon-Sun 11 am - 11 pm"],
    ["Centro", "Mon, Wed-Sun 11 am - 10 pm"],
    ["Brewery Bhavana", "Mon-Sun 11 am - 10:30 pm"],
    ["Dashi", "Mon-Fri 10 am - 9:30 pm / Sat-Sun 9:30 am - 9:30 pm"],
    ["42nd Street Oyster Bar", "Mon-Sat 11 am - 12 am / Sun 12 pm - 2 am"],
    ["Top of the Hill", "Mon-Fri 11 am - 9 pm / Sat 5 pm - 9 pm"],
    ["Jose and Sons", "Mon-Fri 11:30 am - 10 pm / Sat 5:30 pm - 10 pm"],
    ["Oakleaf", "Mon-Thu, Sun 11 am - 10 pm / Fri-Sat 11 am - 11 pm"],
    ["Second Empire", "Mon-Fri 11 am - 10 pm / Sat-Sun 5 pm - 10 pm"]]


def test_NotCorrectPath():
    """
        Should throw FileNotFoundError
    """

    DV = dv.DataValidator()
    try:
        DV.open_file("./testxcvxgsdsgsdav.txt")
        assert(False)
    except FileNotFoundError:
        assert(True)
    except Exception as e:
        assert(False)


def test_Duplication():
    """
        Should throw ValueError
    """

    DV = dv.DataValidator()
    try:
        DV._validation([["test", 0], ["test", 1]])
        assert(False)
    except ValueError:
        assert(True)
    except Exception as e:
        assert(False)


############################# Military Time


def test_MilitaryTime_Non_AM_PM():
    """
        Should throw NotImplementedError
    """

    d = dv.DataValidator()
    try:
        d._to_military_time("11:00 pz")
        assert (False)
    except ValueError:
        assert (True)
    except Exception as e:
        assert (False)


def test_MilitaryTime_Trash1():
    """
        Should throw NotImplementedError
    """

    d = dv.DataValidator()
    try:
        d._to_military_time("11:00")
        assert (False)
    except NotImplementedError:
        assert (True)
    except Exception as e:
        assert (False)


def test_MilitaryTime_Trash1():
    """
        Should throw ValueError
    """

    d = dv.DataValidator()
    try:
        d._to_military_time("27")
        assert (False)
    except ValueError:
        assert (True)
    except Exception as e:
        assert (False)


def test_MilitaryTime_2_digit():

    d = dv.DataValidator()
    t = d._to_military_time("11 pm")
    assert(t == 2300)


def test_MilitaryTime_4_digit():

    d = dv.DataValidator()
    t = d._to_military_time("11:59 pm")
    assert(t == 2359)


def test_MilitaryTime_12AM():

    d = dv.DataValidator()
    t = d._to_military_time("12:01 Am")
    assert(t == 1)


def test_MilitaryTime_1200AM():

    d = dv.DataValidator()
    t = d._to_military_time("12:00 aM")
    assert(t == 0)


def test_MilitaryTime_12PM():

    d = dv.DataValidator()
    t = d._to_military_time("12:59 pm")
    assert(t == 1259)


def test_MilitaryTime_1200PM():

    d = dv.DataValidator()
    t = d._to_military_time("12 pm")
    assert(t == 1200)


############################# Standard Time Format


def test_STF_over12():
    """
        Should throw Value
    """

    d = dv.DataValidator()
    try:
        d._standard_time_format("14 pm")
        assert (False)
    except ValueError:
        assert (True)
    except Exception as e:
        assert (False)

def test_STF_over_5_digits():
    """
        Should throw Value
    """

    d = dv.DataValidator()
    try:
        d._standard_time_format("123:53 pm")
        assert (False)
    except ValueError:
        assert (True)
    except Exception as e:
        assert (False)


############################# _Parse_Time_Chunk

def test_PTC_fake_day_in_range():
    """
        Should throw ValueError
    """

    d = dv.DataValidator()
    try:
        d._parse_time_chunk("XUJ-Fri 11 am - 10 pm")
        assert (False)
    except ValueError:
        assert (True)
    except Exception as e:
        assert (False)

def test_PTC_fake_day():
    """
        Should throw ValueError
    """

    d = dv.DataValidator()
    try:
        d._parse_time_chunk("XUJ 11 am - 10 pm")
        assert (False)
    except ValueError:
        assert (True)
    except Exception as e:
        assert (False)

def test_PTC_two_ranges():
    """
        Should throw ValueError
    """

    d = dv.DataValidator()
    t = d._parse_time_chunk("Mon-Tues,Sat-Sun 11 am - 10 pm")
    print(t)
    assert(t == {'Monday':[1100, 2200],
                'Tuesday': [1100, 2200],
                'Saturday':[1100, 2200],
                'Sunday':[1100, 2200]})






