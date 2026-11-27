class TodoList:
    def __init__(self):
        self.tasks = []

    def get_tasks(self):
        return self.tasks

    def add_task(self, text):
        self.tasks.append({"text": text, "done": False})