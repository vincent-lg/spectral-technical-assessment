"""File containing unittests for the APP."""

from unittest import TestCase
from unittest.mock import MagicMock

from app import app
from blueprints.api import client, collect
from collector_pb2 import ElectricalData

class TestAPP(TestCase):

    """Unittest for the web APP."""

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def test_collect(self):
        """Make sure collect calls the microservice."""
        client.Collect = MagicMock()
        client.Collect.return_value = ElectricalData(states=[])
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
