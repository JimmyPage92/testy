import pytest


def test_should_return_list_todos_increased_after_added_note(todos_fixture):
    from functionality.zadania import add_todo

    content: str = "Go to bed"
    assert add_todo(content) == todos_fixture.append(content)


def test_return_list_todos_without_chosen_to_deleted_note(todos_fixture):
    todos_fixture.remove("Clean my room")
    assert "Clean my room" not in todos_fixture

def test_return_TODOS_with_changed_chosen_note(todos_fixture):
    from functionality.zadania import edit_todo

    content: str = "Get up from bed"
    edit_todo(0, content)

def test_return_empty_list_TODOS_after_deleted_all_notes(todos_fixture):
    from functionality.zadania import remove_all

    assert remove_all() == todos_fixture.clear()

# Zapewnij sprawdzenie przypadków, w których zostanie rzucony wyjątek.
def test_expect_exception_when_TODOS_is_empty():
    from functionality import zadania
    with pytest.raises(zadania.NoMoreTodos):
        zadania.todos = []
        zadania.check_pos(1)

def test_except_exception_when_we_provide_wrong_pos():
    from functionality import zadania
    with pytest.raises(zadania.NoSuchItemNumber):
        zadania.todos = ["some"]
        zadania.check_pos(20)