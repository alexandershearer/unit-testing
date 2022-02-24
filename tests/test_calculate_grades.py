import unittest
from unittest import mock
import pytest
import math
from calculate_grades import *


def test_calculate_stat():
    grade_list = [70, 80, 90, 90, 90]
    mean, standard_deviation = calculate_stat(grade_list)

    assert mean == 84 and standard_deviation == 8


def test_calculate_stat_two():
    grade_list = [65, 72, 84, 93]
    mean, standard_deviation = calculate_stat(grade_list)

    assert mean == 78.5 and math.isclose(standard_deviation, 11, abs_tol = 0.4)
