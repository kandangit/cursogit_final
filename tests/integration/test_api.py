import unittest
from src.app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_tasks(self):
        response = self.app.get('/tasks')
        self.assertEqual(response.status_code, 200)

    def test_add_and_remove_task(self):
        post_response = self.app.post('/tasks', json={'task': 'New Task'})
        self.assertEqual(post_response.status_code, 201)
        delete_response = self.app.delete('/tasks/0')
        self.assertEqual(delete_response.status_code, 204)
        get_response = self.app.get('/tasks')
        self.assertEqual(get_response.json, [])

if __name__ == '__main__':
    unittest.main()
