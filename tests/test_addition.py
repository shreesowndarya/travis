import numpy as np
import pytest
from addition import addition


@pytest.mark.parametrize(
    "x, y",
    [
        (34, 4),
    ],
)
def test_addition(x, y):
    output = 38
    assert addition(x, y) == 38
