def test_should_return_list_todos_increased_after_added_note(todos_fixture):
    from functionality.zadania import add_todo

    content: str = "Go to bed"
    assert add_todo(content) == todos_fixture.append(content)


def test_return_list_todos_without_chosen_to_deleted_note(todos_fixture):
    todos_fixture.remove("Clean my room")
    assert "Clean my room" not in todos_fixture


def test_return_TODOS_with_changed_chosen_note():
    from functionality.zadania import edit_todo

    content: str = "Get up from bed"
    edit_todo(0, content)


def test_return_empty_list_TODOS_after_deleted_all_notes(todos_fixture):
    from functionality.zadania import remove_all

    assert remove_all() == todos_fixture.clear()
