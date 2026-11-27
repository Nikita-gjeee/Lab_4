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

    def count_tasks(self):
        return len(self.tasks)

    def get_done_tasks(self):
        return [task for task in self.tasks if task["done"]]

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task["done"]]

    def edit_task(self, index, new_text):
        self.tasks[index]["text"] = new_text

    def find_tasks(self, keyword):
        return [task for task in self.tasks if keyword.lower() in task["text"].lower()]