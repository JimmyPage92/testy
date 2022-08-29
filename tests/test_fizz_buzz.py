import pytest


@pytest.mark.parametrize(
    "num, expected_fizz_results",
    [
        (3, "FIZZ"),
        (10, "BUZZ"),
        (15, "fizzbuzz"),
    ],
)
def test_fizz_buzz(num: int, expected_fizz_results: str):
    from functionality.zadania import fizz_buzz

    assert fizz_buzz(num) == expected_fizz_results

