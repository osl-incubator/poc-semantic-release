"""Tests for `poc_semantic_release` package."""

import random

import pytest

from poc_semantic_release import poc_semantic_release


@pytest.fixture
def generate_numbers():
    """
    Sample pytest fixture. Generates list of random integers.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """

    return random.sample(range(100), 10)


def test_sum_numbers(generate_numbers):
    """Sample test function for sum_numbers, using pytest fixture."""

    our_result = poc_semantic_release.sum_numbers(generate_numbers)
    assert our_result == sum(generate_numbers)


def test_max_number(generate_numbers):
    """Sample test function for max_number, using pytest fixture."""

    our_result = poc_semantic_release.max_number(generate_numbers)
    assert our_result == max(generate_numbers)
