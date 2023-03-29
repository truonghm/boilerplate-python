from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


class TestMainAPI:
    def test_read_root(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"msg": "Streamlit Backend APIs"}
