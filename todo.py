class TodoList:
    def __init__(self):
        self.tasks = []

    def get_tasks(self):
        return self.tasks

    def add_task(self, text):
        self.tasks.append({"text": text, "done": False})

    def mark_done(self, index):
        self.tasks[index]["done"] = True

    def delete_task(self, index):
        del self.tasks[index]

    def clear_tasks(self):
        self.tasks.clear()