import pytest


# class TestIsPrime:
#     def test_should_return_YES_when_we_provide_first_num(self):
#         """Zadania one tests."""
#         from functionality.zadania import is_num_prime
#
#         assert is_num_prime(num=5) is True
#
#
# def test_should_return_YES_when_we_provide_first_num():
#     """Tests without class."""
#     from functionality.zadania import is_num_prime
#
#     assert is_num_prime(num=5) is True
#
#
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
#
#
# def test_should_sorted_elements_after_used_method_quick_sort():
#     from functionality.zadania import quick_sort_method
#     assert quick_sort_method([8, 7, 6, 1, 0, 9, 2]) == [0, 1, 2, 6, 7, 8, 9]
#
#
# # zad.4
# # korzystam z pytest.fixture ktora bedzie automatycznie generować sobie dane i pracować bez
# # żadnych wewnętrznych powiązań
#
#

# #
# #
# #
# #
# # Zapewnij sprawdzenie przypadków, w których zostanie rzucony wyjątek.
# def test_expect_exception_when_TODOS_is_empty():
#     with pytest.raises(zadania.NoMoreTodos):
#         zadania.todos = []
#         zadania.check_pos(1)
#
#
# #
# def test_except_exception_when_we_provide_wrong_pos():
#     with pytest.raises(zadania.NoSuchItemNumber):
#         zadania.todos = ["some"]
#         zadania.check_pos(20)
#
#
# @freeze_time("2022-08-27 20:00:00", tz_offset=0)
# def test_freeze_time():
#     from functionality.zadania import calc_diff
#
#     case = {
#         "start_time": "2021-11-03T09:22:28+00:00",
#         "end_time": None,  # None means that case is currently going on
#     }
#     assert datetime.now() == datetime(2022, 8, 27, 20, 0, 0)
#
#     start_time_obj = datetime.fromisoformat("2021-11-03T09:22:28+00:00")
#     timer = (datetime.now(timezone.utc) - start_time_obj).total_seconds()
#
#     assert timer == calc_diff(case)
