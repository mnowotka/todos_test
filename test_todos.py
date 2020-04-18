import os
import unittest
from unittest.mock import Mock, patch
from nose.tools import assert_is_not_none, assert_list_equal
from service import Service
from schema import TodoSchema


class TestTodos(unittest.TestCase):

    def setUp(self):
        if os.getenv('TEST_REAL_API', False):
            return
        self.mock_get_patcher = patch('service.requests.get')
        self.mock_get = self.mock_get_patcher.start()

        self.expected_todos = [{
            'userId': 1,
            'id': 1,
            'title': 'Make the bed',
            'completed': False
        }]

        self.mock_get.return_value = Mock(ok=True)
        self.mock_get.return_value.json.return_value = self.expected_todos

    def tearDown(self):
        if os.getenv('TEST_REAL_API', False):
            return
        self.mock_get_patcher.stop()

    def test_getting_todos(self):
        todo = Service.get_todos()
        assert_is_not_none(todo)
        assert_list_equal(todo, self.expected_todos)
        TodoSchema().load(many=True, data=todo)
