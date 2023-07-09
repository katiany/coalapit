from unittest import TestCase
from src.api.controller.coalesce import coalesce
from src.api.model.response import Response


class TestCoalesce(TestCase):
    def test_coalesce(self):
        actual = coalesce(data=[
            {"deductible": 1000, "stop_loss": 10000, "oop_max": 5000},
            {"deductible": 1200, "stop_loss": 13000, "oop_max": 6000},
            {"deductible": 1000, "stop_loss": 10000, "oop_max": 6000}
        ])

        averages = {"deductible": 1066, "stop_loss": 11000, "oop_max": 5666}

        expected = Response(**averages)

        self.assertEqual(actual, expected)
