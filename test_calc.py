"""Tests for the tiny calculator."""

import pytest

import calc


def test_divide_by_zero_raises_value_error():
    with pytest.raises(ValueError, match="cannot divide by zero"):
        calc.divide(1, 0)
