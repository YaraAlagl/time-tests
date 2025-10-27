import pytest
from times import time_range, compute_overlap_time


def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [(
        '2010-01-12 10:30:00', '2010-01-12 10:37:00'), 
        ('2010-01-12 10:38:00', '2010-01-12 10:45:00')
        ]
    assert result == expected

def test_no_overlap():
    range1 = time_range("2022-01-01 10:00:00", "2022-01-01 11:00:00")
    range2 = time_range("2022-01-01 12:00:00", "2022-01-01 13:00:00")
    result = compute_overlap_time(range1, range2)
    expected = []
    assert result == expected

def test_several_intervals():
    range1 = time_range("2022-01-01 10:00:00", "2022-01-01 12:00:00", 2,0)
    range2 = time_range("2022-01-01 11:00:00", "2022-01-01 13:00:00", 2,0)
    result = compute_overlap_time(range1, range2)
    expected = [
        ('2022-01-01 11:00:00', '2022-01-01 12:00:00')
    ]
    assert result == expected

def test_starts_at_end():
    range1 = time_range("2022-01-01 10:00:00", "2022-01-01 11:00:00")
    range2 = time_range("2022-01-01 11:00:00", "2022-01-01 12:00:00")
    result = compute_overlap_time(range1, range2)
    expected = []
    assert result == expected

def test_ends_before_start():
     with pytest.raises(ValueError, match="end_time must be after start_time"):
        time_range("2022-01-01 12:00:00", "2022-01-01 10:00:00")


@pytest.mark.parametrize("time_range1,time_range2,expected", [
    (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
     time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60), 
     [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), 
        ('2010-01-12 10:38:00', '2010-01-12 10:45:00')])，
        ])
def test_eval(time_range1, time_range2, expected):
    assert compute_overlap_time(time_range1, time_range2) == expected
        