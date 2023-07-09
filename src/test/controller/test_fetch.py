from unittest import TestCase
from unittest.mock import patch
from src.api.config import Settings
from src.api.controller.fetch import fetch_data
from src.api.model.response import Response


class TestFetch(TestCase):
    @patch('src.api.controller.fetch.get')
    def test_fetch_data(self, get_mock):

        actual = fetch_data(member_id=1)

        get_mock.return_value = {"deductible": 1000, "stop_loss": 10000, "oop_max": 5000}

        self.assertEqual(len(actual), 3)
        self.assertEqual(get_mock.call_count, 3)
