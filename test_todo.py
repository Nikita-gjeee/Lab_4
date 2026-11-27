from todo import TodoList

def test_empty_todo_list():
    todo = TodoList()
    assert todo.get_tasks() == []

def test_add_task():
    todo = TodoList()
    todo.add_task("Купить хлеб")
    assert len(todo.get_tasks()) == 1
    assert todo.get_tasks()[0]["text"] == "Купить хлеб"