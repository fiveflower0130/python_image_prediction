from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"data": "Hello World"}


def test_get_image_prediction():
    expect = {
        "code": "0",
        "message": "",
        "data": [
            {
                "image": "L201030128_金面汙染_Total_35.png",
                "prediction": "strip",
                "probability": "97.84570932388306"
            }
        ]
    }
    headers = {"x-token": "coneofsilence"}
    body = {"path": "L201030128_金面汙染_Total_35.png"}
    resp = client.post("/image/prediction", json=body, headers=headers)
    # body = {}
    # resp = client.get("/image/prediction?path=L201030128_金面汙染_Total_35.png", json=body, headers=headers)
    assert resp.status_code == 200
    assert resp.json() == expect
