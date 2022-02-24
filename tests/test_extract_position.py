import pytest
from ..extract_position import extract_position


def testExtractPosition():
    line1 = '|error| numerical calculations could not converge.'
    line2 = '|update| the positron location in the particle accelerator is x:21.432'

    assert extract_position(line1) == None
    assert extract_position(line2) == '21.432'