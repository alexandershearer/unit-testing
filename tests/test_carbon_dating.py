import unittest
import pytest
import math
from ..carbon_dating import get_age_carbon_14_dating

# Write a unit test which feed 0.35 to the function.
# The result should be '8680.34'. Does the function handles
# every possible input correctly? What if the input is zero
# or negative?
# Add the necessary logic to make sure the function handle
# every possible input properly. Then write a unit test againt
# this special case.


def testCarbonDating():
    carbon14ratio=.35
    # check if 0 or negative
    if carbon14ratio <= 0:
        assert False
        return
    # check if not int or float
    if type(carbon14ratio) != 'int' or type(carbon14ratio) != 'float':
        assert False
        return
    assert math.isclose(get_age_carbon_14_dating(carbon14ratio), 8680.34, abs_tol=0.05)

