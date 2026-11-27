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

def test_delete_task():
    todo = TodoList()
    todo.add_task("Задача 1")
    todo.add_task("Задача 2")
    todo.delete_task(0)
    assert len(todo.get_tasks()) == 1
    assert todo.get_tasks()[0]["text"] == "Задача 2"

def test_clear_all_tasks():
    todo = TodoList()
    todo.add_task("Задача 1")
    todo.add_task("Задача 2")
    todo.clear_tasks()
    assert todo.get_tasks() == []

def test_count_tasks():
    todo = TodoList()
    todo.add_task("A")
    todo.add_task("B")
    assert todo.count_tasks() == 2

def test_get_done_tasks():
    todo = TodoList()
    todo.add_task("Сделано")
    todo.add_task("Не сделано")
    todo.mark_done(0)
    done_tasks = todo.get_done_tasks()
    assert len(done_tasks) == 1
    assert done_tasks[0]["text"] == "Сделано"

def test_get_pending_tasks():
    todo = TodoList()
    todo.add_task("Сделано")
    todo.add_task("Не сделано")
    todo.mark_done(0)
    pending = todo.get_pending_tasks()
    assert len(pending) == 1
    assert pending[0]["text"] == "Не сделано"