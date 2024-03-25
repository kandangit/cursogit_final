_tasks = []

def get_tasks():
    return _tasks

def add_task(task):
    _tasks.append(task)

def remove_task(task_id):
    _tasks.pop(task_id)
