from lib.check_age import *
import pytest

def test_if_given_the_wrong_format_raise_exception():
    with pytest.raises(Exception) as e: 
        check_age('21/04/15')
    assert str(e.value) == "Exception - incorrect format"

def test_correct_format_but_under_age():
    assert check_age("2020-02-05") == "ACCESS DENIED! You are 4, but need to be 16 to access."

def test_correct_format_and_over_age():
    assert check_age("1984-02-09") == "ACCESS GRANTED! You are 39."

def test_correct_format_and_under_age_cusp():
    assert check_age("2008-02-06") == "ACCESS DENIED! You are 15, but need to be 16 to access."

def test_correct_format_and_over_age_cusp():
    assert check_age("2008-02-05") == "ACCESS GRANTED! You are 16."
