#!/usr/bin/env python3
"""unittest file for testing utils module"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
import utils
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    """Class for testing the utils.py methods"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test for utils.access_nested_map method"""
        result = utils.access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_exception):
        """Test for access_nested_map exception"""
        with self.assertRaises(expected_exception):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class for testing the utils.get_json method"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, url, payload, mock_get):
        """Test for the get_json return"""
        mock_response = Mock()
        mock_response.json.return_value = payload
        mock_get.return_value = mock_response

        result = utils.get_json(url)

        self.assertEqual(result, payload)
        mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """Class for testing the utils.memoize"""

    def test_memoize(self):
        """Test for memoize decorator"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        obj = TestClass()
        with patch.object(obj, 'a_method', return_value=42) as mock_method:
            r1 = obj.a_property
            r2 = obj.a_property

            self.assertEqual(r1, 42)
            self.assertEqual(r2, 42)

            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
