"""Module containing the unittest for the data collector service."""

from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from server import DataCollectorService

class TestCollector(TestCase):

    """Unittest containing tests for the data collector service."""

    @patch("server.open")
    def test_collect_empty(self, mock_open):
        """An empty file should yield no result from Collect."""
        mock_open.return_value = StringIO("")
        service = DataCollectorService()
        state = service.Collect(None, None)
        self.assertEqual(list(state.states), [])

    @patch("server.open")
    def test_collect_one(self, mock_open):
        """Try to collect from a CSV with only one line."""
        mock_open.return_value = StringIO("time,meter")
        service = DataCollectorService()
        state = service.Collect(None, None)
        self.assertEqual(list(state.states), [])

        # Run the same test with a new line.
        mock_open.return_value = StringIO("time,meter\n")
        service = DataCollectorService()
        state = service.Collect(None, None)
        self.assertEqual(list(state.states), [])

    @patch("server.open")
    def test_collect_valid(self, mock_open):
        """Test to collect a valid mocked file."""
        mock_open.return_value = StringIO(
                "time,meter\n"
                "2021-01-01 00:00:00,30"
        )
        service = DataCollectorService()
        state = service.Collect(None, None)
        self.assertEqual(len(state.states), 1)
        unique = state.states[0]
        self.assertIsNotNone(unique.step)
        self.assertEqual(unique.meter, 30.0)

        # Test to collect with two lines (besides the header).
        mock_open.return_value = StringIO(
                "time,meter\n"
                "2021-01-01 00:00:00,30\n"
                "2021-01-01 00:15:00,35\n"
        )
        service = DataCollectorService()
        state = service.Collect(None, None)
        self.assertEqual(len(state.states), 2)
        first, second = state.states
        self.assertIsNotNone(first.step)
        self.assertEqual(first.meter, 30.0)
        self.assertIsNotNone(second.step)
        self.assertEqual(second.meter, 35.0)

    @patch("server.open")
    def test_collect_invalid(self, mock_open):
        """Make sure an incorrect CSV won't break the test."""
        mock_open.return_value = StringIO(
                "time,meter\n"
                "2021-01-01 00:00:00;30"
        )
        service = DataCollectorService()
        state = service.Collect(None, None)
        self.assertEqual(len(state.states), 0)

        # Run the same test, but with one valid and invalid line.
        mock_open.return_value = StringIO(
                "time,meter\n"
                "that's an invalid line\n"
                "2021-01-01 00:00:00,30\n"
                "2021-01-01 00:15:00,invalid float\n"
                "invalid time,41\n"
        )
        service = DataCollectorService()
        state = service.Collect(None, None)
        self.assertEqual(len(state.states), 1)
        unique = state.states[0]
        self.assertIsNotNone(unique.step)
        self.assertEqual(unique.meter, 30.0)
