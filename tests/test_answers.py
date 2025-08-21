import unittest
from fastapi.testclient import TestClient
import io
import polars as pl
from app.main import app

client = TestClient(app)


class AnswersTestCase(unittest.TestCase):
    def generate_csv_bytes(self, headers: list[str], rows: list[dict]) -> bytes:
        """Gera um CSV em bytes a partir de headers e linhas."""
        tabela = pl.DataFrame(rows)[headers]
        buf = io.BytesIO()
        tabela.write_csv(buf)
        return buf.getvalue()

    def test_answser_correctly(self):
        csv = self.generate_csv_bytes(
            ["name", "age"],
            [
                {"name": "leo", "age": "18"},
                {"name": "keven", "age": "20"},
                {"name": "ramon", "age": "22"},
            ],
        )
        res = client.post(
            "/answer/",
            json={"questionID": 1, "userID": 1},
            files={"file": ("clientes.csv", csv, "text/csv")},
        )
        json = res.json()
        print(json)
        assert json["success"]
        assert json["score"] == 100

    def test_answser_incorrectly(self):
        csv = self.generate_csv_bytes(
            ["name", "age"],
            [
                {"name": "leo", "age": "118"},
                {"name": "keven", "age": "20"},
                {"name": "ramon", "age": "22"},
            ],
        )
        res = client.post(
            "/answer/",
            json={"questionID": 1, "userID": 1},
            files={"file": ("clientes.csv", csv, "text/csv")},
        )
        assert res.status_code == 422, res.status_code
