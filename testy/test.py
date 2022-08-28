from functionality import zadania
import pytest
import typing as tp
from freezegun import freeze_time
from datetime import datetime, timezone

#zad 1
# z uzyciem klasy
class TestIsPrime:

    def test_should_return_YES_when_we_provide_first_num(self):
        num = 5

        assert zadania.is_num_prime(num) == True

#bez uzycia klasy
def test_should_return_YES_when_we_provide_first_num():
    num = 5

    assert zadania.is_num_prime(num) == True

#zad_2
def test_should_return_FIZZ_when_we_provide_num_divide_by_3():
    num = 3

    assert zadania.fizz_buzz(num) == 'FIZZ'

def test_should_return_BUZZ_when_we_provide_num_divide_by_5():
    num = 10

    assert zadania.fizz_buzz(num) == 'BUZZ'

def test_should_return_FIZZBUZZ_when_we_provide_num_divide_by_5_and_3():
    num = 15

    assert zadania.fizz_buzz(num) == 'fizzbuzz'

#zad.3
def test_should_sorted_elements_after_used_method_quick_sort():
    list = [8,7,6,1,0,9,2]

    assert zadania.quick_sort_method(list) == [0,1,2,6,7,8,9]

#zad.4
#korzystam z pytest.fixture ktora bedzie automatycznie generować sobie dane i pracować bez
#żadnych wewnętrznych powiązań

@pytest.fixture
def todos() -> tp.List[str]:
    return ["Clean my room", "Make my bed", "Go to school", "Do school homework"]

def test_should_return_list_todos_increased_after_added_note(todos):
    content: str = ('Go to bed')
    assert zadania.add_todo(content) == todos.append(content)

def test_return_list_todos_without_chosen_to_deleted_note(todos):
    todos.remove("Clean my room")
    assert "Clean my room" not in todos

def test_return_TODOS_with_changed_chosen_note(todos):
    content: str = "Get up from bed"
    zadania.edit_todo(0, content)

def test_return_empty_list_TODOS_after_deleted_all_notes(todos):
    assert zadania.remove_all() == todos.clear()

# Zapewnij sprawdzenie przypadków, w których zostanie rzucony wyjątek.
def test_expect_exception_when_TODOS_is_empty():
    with pytest.raises(zadania.NoMoreTodos):
        zadania.todos = []
        zadania.check_pos(1)

def test_except_exception_when_we_provide_wrong_pos():
     with pytest.raises(zadania.NoSuchItemNumber):
        zadania.todos=['some']
        zadania.check_pos(-1)
#zad 5

@freeze_time("2022-08-28 20:00:00", tz_offset=0)
def test_freeze_time():
    case = {
        'start_time': '2021-11-03T09:22:28+00:00',
        'end_time': None  # None means that case is currently going on
    }
    assert datetime.now() == datetime(2022, 8, 28, 20, 0, 0)
    start_time = '2021-11-03T09:22:28+00:00'
    start_time_obj = datetime.fromisoformat(start_time)
    timer = (datetime.now(timezone.utc) - start_time_obj).total_seconds()

    assert timer == zadania.calc_diff(case)

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

