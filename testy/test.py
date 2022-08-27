import functionality.zadania
from functionality.zadania import *

import pytest


#zad 1
# z uzyciem klasy
class TestIsPrime:

    def test_should_return_YES_when_we_provide_first_num(self):
        num = 5

        assert is_num_prime(num) == True

#bez uzycia klasy
def test_should_return_YES_when_we_provide_first_num():
    num = 5

    assert is_num_prime(num) == True

#zad_2
def test_should_return_FIZZ_when_we_provide_num_divide_by_3():
    num = 3

    assert fizz_buzz(num) == 'FIZZ'

def test_should_return_BUZZ_when_we_provide_num_divide_by_5():
    num = 10

    assert fizz_buzz(num) == 'BUZZ'

def test_should_return_FIZZBUZZ_when_we_provide_num_divide_by_5_and_3():
    num = 15

    assert fizz_buzz(num) == 'fizzbuzz'

#zad.3
def test_should_sorted_elements_after_used_method_quick_sort():
    list = [8,7,6,1,0,9,2]

    assert quick_sort_method(list) == [0,1,2,6,7,8,9]


#zad.4
# Zapewnij sprawdzenie przypadków, w których zostanie rzucony wyjątek.

def test_expect_exception_when_TODOS_is_empty():
    with pytest.raises(Exception):
        assert check_pos()

def test_except_exception_when_we_provide_wrong_pos():
    with pytest.raises(NoSuchItemNumber) as exc:

        assert 'list index out of range' == str(exc.value)


def test_should_return_list_todos_increased_after_added_note():
    todos = ["Clean my room", "Make my bed", "Go to school", "Do school homework"]
    content = ('Go to bed')

    assert add_todo(content) == todos.append(content)

def test_return_list_todos_without_chosen_to_deleted_note():
    todos = ["Clean my room", "Make my bed", "Go to school", "Do school homework"]
    pos = todos[0]
    todos.remove(pos)
    assert "Clean my room" not in todos

def test_return_TODOS_with_changed_chosen_note(): #### rzuca blad
    # todos = ["Get up from bed", "Make my bed", "Go to school", "Do school homework"]
    pos = 0

    content = "Get up from bed"
    edit_todo(pos, content)
    assert content in todos


def test_return_empty_list_TODOS_after_deleted_all_notes():
    assert remove_all() == todos.clear()

#zad 5

def test_calc_diff(mocker):
    case = {
        'start_time': '2021-11-03T09:22:28+00:00',
        'end_time': None  # None means that case is currently going on
    }
    mocker.patch('functionality.zadania.get_datetimenow',return_value=datetime.now(timezone.utc))
    time_1 = datetime.fromisoformat('2021-11-03T09:22:28+00:00')
    time_end = datetime.now(timezone.utc)

    expected = (time_end - time_1).total_seconds()

    assert calc_diff(case) == expected

#zad. 6
#czy w tym zadaniu najpierw trzeba zamokowac STALE z klasy Config ?? i dopiero przetestowac klase
# DBHANDLER

# def test_class_config(mocker):
#
#     mocker.patch.object(functionality.zadania.Config, 'DB_URL', config('DB_URL'))
#     expected='DB_URL'
#     actual=Config()
#
#     assert expected == actual

def test_class_dbhandler():
    pass
