import json

bicycle_data = {
    "model": "testapimodel",
    "brand": "testapibrand",
    "price": "200",
    "description": "testapidescription",
    "image": "testapiimage",
}

bicyle1_id = None


def test_create_bicycle(client):
    global bicycle1_id
    response = client.post(
        "api/v1/bicycle",
        data=json.dumps(bicycle_data),
        content_type="application/json",
    )
    bicycle1_id = response.json["id"]
    assert response.status_code == 201
    assert response.json["brand"] == "testapibrand"
    assert response.json["price"] == "200"
    assert response.json["image"] == "testapiimage"


def test_request_bicycles(client):
    response = client.get("api/v1/bicycle")
    assert isinstance(response.json, list) is True
    assert len(response.json) == 1
    assert response.json[0]["brand"] == "testapibrand"
    assert response.json[0]["price"] == 200.0


def test_request_bicycle(client):
    global bicycle1_id
    response = client.get(f"api/v1/bicycle/{bicycle1_id}")
    assert isinstance(response.json, dict) is True
    assert response.json["id"] == bicycle1_id
    assert response.json["brand"] == "testapibrand"
    assert response.json["price"] == 200.0


def test_update_bicycle(client):
    global bicycle1_id
    update_data = json.dumps(
        {"model": "updatedapimodel", "brand": "updatedapibrand"}
    )
    response = client.put(
        f"api/v1/bicycle/{bicycle1_id}",
        data=update_data,
        content_type="application/json",
    )

    assert response.status_code == 200

    response = client.get(f"api/v1/bicycle/{bicycle1_id}")
    assert response.json["id"] == bicycle1_id
    assert response.json["model"] == "updatedapimodel"
    assert response.json["brand"] == "updatedapibrand"


def test_delete_bicycle(client):
    global bicycle1_id
    response = client.delete(f"api/v1/bicycle/{bicycle1_id}")
    assert response.status_code == 200
    assert response.json == [{}, 200]
