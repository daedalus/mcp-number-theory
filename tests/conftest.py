"""Pytest configuration for mcp-number-theory tests."""

import pytest


@pytest.fixture
def sample_prime():
    return 7919


@pytest.fixture
def sample_composite():
    return 7919 * 7907


@pytest.fixture
def small_primes():
    return [2, 3, 5, 7, 11, 13, 17, 19, 23]
