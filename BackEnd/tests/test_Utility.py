""""

    Author: Thomas Theis, 2021

"""


import sys, os

# Make sure that the application source directory (this directory's parent) is
# on sys.path.

here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, here)

from Utility import Utility as u


def test_Utility_key_by_index_junk1():
    try:
        k = u.key_by_index({'hello': 'world'}, 'no')
        assert(False)
    except ValueError:
        assert(True)
    except Exception as e:
        assert(False)


def test_Utility_key_by_index_junk2():
    try:
        k = u.key_by_index({'hello': 'world'}, None)
        assert(False)
    except ValueError:
        assert(True)
    except Exception as e:
        assert(False)

def test_Utility_key_by_index_junk3():
    try:
        k = u.key_by_index({'hello': 'a'}, "")
        assert(False)
    except ValueError:
        assert(True)
    except Exception as e:
        assert(False)

def test_Utility_key_by_index_junk4():
    try:
        k = u.key_by_index({'hello': 'a'}, 97)
        assert(False)
    except ValueError:
        assert(True)
    except Exception as e:
        assert(False)

def test_Utility_key_by_index_junk4():
    try:
        k = u.key_by_index({None: None}, 'a')
        assert(False)
    except ValueError:
        assert(True)
    except Exception as e:
        assert(False)

def test_Utility_key_by_index_two_keys():
    k = u.key_by_index({'hello': 1, 'world': 1}, 1)
    assert(isinstance(k, str))


###################################### first_digit_index

def test_fdi_no_digit1():
    try:
        k = u.first_digit_index('f')
        assert(False)
    except ValueError:
        assert(True)
    except Exception as e:
        assert(False)

def test_fdi_no_digit1():
    try:
        k = u.first_digit_index('')
        assert(False)
    except ValueError:
        assert(True)
    except Exception as e:
        assert(False)
