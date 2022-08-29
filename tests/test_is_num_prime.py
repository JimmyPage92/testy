import pytest


class TestIsPrime:
    def test_should_return_YES_when_we_provide_first_num(self):
        """Zadania one tests."""
        from functionality.zadania import is_num_prime

        assert is_num_prime(num=5) is True


def test_should_return_YES_when_we_provide_first_num():
    """Tests without class."""
    from functionality.zadania import is_num_prime

    assert is_num_prime(num=5) is True

