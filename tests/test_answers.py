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

    def test_answer_missing_question(self):
        payload = {
            "question_id": 999999,  # unlikely to exist
            "answer": [{"linha": {}}],
        }
        res = client.post("/answer/", json=payload)
        self.assertIn(res.status_code, (404, 400))

    def test_answer_missing_fields(self):
        payload = {
            # missing question_id and answer
        }
        res = client.post("/answer/", json=payload)
        self.assertEqual(res.status_code, 422)

    def test_answer_with_empty_answer(self):
        payload = {
            "question_id": self.latestQuestionID,
            "answer": [],
        }
        res = client.post("/answer/", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertFalse(data["success"])
        self.assertEqual(data["score"], 0)
