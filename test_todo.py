from todo import TodoList

def test_empty_todo_list():
    todo = TodoList()
    assert todo.get_tasks() == []

def test_add_task():
    todo = TodoList()
    todo.add_task("Купить хлеб")
    assert len(todo.get_tasks()) == 1
    assert todo.get_tasks()[0]["text"] == "Купить хлеб"

def test_task_is_not_done_by_default():
    todo = TodoList()
    todo.add_task("Помыть посуду")
    assert todo.get_tasks()[0]["done"] is False

def test_mark_task_as_done():
    todo = TodoList()
    todo.add_task("Сделать уроки")
    todo.mark_done(0)
    assert todo.get_tasks()[0]["done"] is True