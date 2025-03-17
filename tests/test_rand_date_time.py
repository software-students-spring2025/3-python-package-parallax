from fortune_teller.main import rand_date_time
import pytest


def test_rand_date_time():
    result = rand_date_time("Test fortune")
    assert "Test fortune" in result
    assert "📅 On " in result  # Ensures date formatting is present