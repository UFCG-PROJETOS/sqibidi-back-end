import unittest
from fastapi.testclient import TestClient
import io
import polars as pl
from app.main import app

client = TestClient(app)


class AnswersTestCase(unittest.TestCase):
    def setUp(self):
        payload = {
            "name": "string",
            "code": "string",
            "type_question": "SELECT",
            "expected_answer": [{"linha": {}}],
        }
        res = client.post("/question/", json=payload)
        self.latestQuestionID = res.json()["id"]

    def test_answser_correctly(self):
        payload = {
            "question_id": self.latestQuestionID,
            "answer": [{"linha": {}}],
        }
        res = client.post(
            "/answer/",
            json=payload,
        )
        json = res.json()
        assert res.status_code == 200, res.status_code
        assert json["success"]
        assert json["score"] == 100

    def test_answser_incorrectly(self):
        payload = {
            "question_id": self.latestQuestionID,
            "answer": [{"asdasdads": {}}],
        }
        res = client.post(
            "/answer/",
            json=payload,
        )
        assert res.status_code == 200, res.status_code
        json = res.json()
        assert not json["success"]
        assert json["score"] == 0
