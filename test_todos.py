from unittest.mock import patch

from nose.tools import assert_is_not_none

from service import Service

def test_getting_todos():
    with patch('service.requests.get') as mock_get:
        mock_get.return_value.ok = True
        todo = Service.get_todos()
        assert_is_not_none(todo)
