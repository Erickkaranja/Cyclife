import json

client_data = {
    "email": "testapiemail",
    "password": "testapipassword",
    "first_name": "testapifname",
    "last_name": "testapilname",
}

user1_id = None


def test_create_user(client):
    global user1_id
    response = client.post(
        "api/v1/user",
        data=json.dumps(client_data),
        content_type="application/json",
    )
    user1_id = response.json["id"]
    assert response.status_code == 201
    assert response.json["email"] == "testapiemail"
    assert response.json["first_name"] == "testapifname"


def test_request_users(client):
    response = client.get("api/v1/user")
    assert isinstance(response.json, list) is True
    assert len(response.json) == 1


def test_request_user(client):
    global user1_id
    response = client.get(f"api/v1/user/{user1_id}")
    assert isinstance(response.json, dict) is True
    assert response.json["id"] == user1_id


def test_update_user(client):
    global user1_id
    update_data = json.dumps(
        {"first_name": "updatedfname", "email": "updatedemail"}
    )
    response = client.put(
        f"api/v1/user/{user1_id}",
        data=update_data,
        content_type="application/json",
    )

    assert response.status_code == 200

    response = client.get(f"api/v1/user/{user1_id}")
    assert response.json["id"] == user1_id
    assert response.json["first_name"] == "updatedfname"
    assert response.json["email"] == "updatedemail"


def test_delete_user(client):
    global user1_id
    response = client.delete(f"api/v1/user/{user1_id}")
    assert response.status_code == 200
    assert response.json == [{}, 200]
