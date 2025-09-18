import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class QuestionsTestCase(unittest.TestCase):
    pass
