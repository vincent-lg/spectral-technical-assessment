"""File containing unittests for the API."""

from unittest import TestCase
from unittest.mock import MagicMock

from app import app
from blueprints.api import client, collect
from collector_pb2 import ElectricalData

class TestAPI(TestCase):

    """Unittest for the web API."""

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def test_collect(self):
        """Make sure collect calls the microservice."""
        client.Collect = MagicMock()
        client.Collect.return_value = ElectricalData(states=[])
        response = self.app.get("/api/collect")
        self.assertEqual(response.json, [])
