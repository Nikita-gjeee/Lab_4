from todo import TodoList

def test_empty_todo_list():
    todo = TodoList()
    assert todo.get_tasks() == []