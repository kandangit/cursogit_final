import unittest
from src.tasks import add_task, get_tasks, remove_task


class TestTasks(unittest.TestCase):
    def test_add_task(self):
        add_task('Learn Python')
        self.assertIn('Learn Python', get_tasks())

    def test_remove_task(self):
        add_task('Learn Flask')
        remove_task(-1)
        self.assertNotIn('Learn Flask', get_tasks())


if __name__ == '__main__':
    unittest.main()
