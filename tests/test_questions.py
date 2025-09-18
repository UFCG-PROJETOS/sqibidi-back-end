import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class QuestionsTestCase(unittest.TestCase):
    def setUp(self):
        self.payload = {
            "name": "Test Question",
            "code": "SELECT * FROM test;",
            "type_question": "SELECT",
            "expected_answer": [{"linha": {}}],
        }
        res = client.post("/question/", json=self.payload)
        self.assertEqual(res.status_code, 200)
        self.question = res.json()
        self.question_id = self.question["id"]

    def test_create_question(self):
        payload = {
            "name": "Another Question",
            "code": "SELECT 1;",
            "type_question": "SELECT",
            "expected_answer": [{"linha": {}}],
        }
        res = client.post("/question/", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["name"], payload["name"])
        self.assertEqual(data["code"], payload["code"])
        self.assertEqual(data["type_question"], payload["type_question"])
        self.assertEqual(data["expected_answer"], payload["expected_answer"])

    def test_get_question(self):
        res = client.get(f"/question/{self.question_id}/")
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["id"], self.question_id)
        self.assertEqual(data["name"], self.payload["name"])

    def test_list_questions(self):
        res = client.get("/question/")
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertIsInstance(data, list)
        self.assertTrue(any(q["id"] == self.question_id for q in data))

    def test_update_question(self):
        update_payload = {
            "id": self.question_id,
            "name": "Updated Name",
            "code": "SELECT 2;",
            "type_question": "SELECT",
            "expected_answer": [{"linha": {}}],
        }
        res = client.put(f"/question/{self.question_id}/", json=update_payload)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["name"], "Updated Name")
        self.assertEqual(data["code"], "SELECT 2;")

    def test_delete_question(self):
        payload = {
            "name": "To Delete",
            "code": "SELECT 3;",
            "type_question": "SELECT",
            "expected_answer": [{"linha": {}}],
        }
        res = client.post("/question/", json=payload)
        self.assertEqual(res.status_code, 200)
        question_id = res.json()["id"]

        res = client.delete(f"/question/{question_id}/")
        self.assertEqual(res.status_code, 200)

        res = client.get(f"/question/{question_id}/")
        self.assertEqual(res.status_code, 404)

    def test_set_and_get_day_question(self):
        res = client.post(f"/question/day_question/?id={self.question_id}")
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["id"], self.question_id)

        res = client.get("/question/day_question/")
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["id"], self.question_id)
        self.assertNotIn("expected_answer", data)
