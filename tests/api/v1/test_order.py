import json

user1_id = None
bicycle1_id = None
order1_id = None

bicycle_data = {
    "model": "testapimodel_order",
    "brand": "testapibrand_order",
    "price": "200",
    "description": "testapidescription_order",
    "image": "testapiimage_order",
}

user_data = {
    "email": "testapiemail_order",
    "password": "testapipassword_order",
    "first_name": "testapifname_order",
    "last_name": "testapilname_order",
}


def test_create_order(client):
    global user1_id
    global bicycle1_id
    global order1_id
    response = client.post(
        "api/v1/user",
        data=json.dumps(user_data),
        content_type="application/json",
    )
    user1_id = response.json["id"]
    response = client.post(
        "api/v1/bicycle",
        data=json.dumps(bicycle_data),
        content_type="application/json",
    )
    bicycle1_id = response.json["id"]
    order_data = {
        "order_status": "Pending",
        "total_price": 400,
        "bicycle_id": bicycle1_id,
        "user_id": user1_id,
    }
    response = client.post(
        f"api/v1/user/{user1_id}/order",
        data=json.dumps(order_data),
        content_type="application/json",
    )
    order1_id = response.json["id"]
    assert response.status_code == 201
    assert isinstance(response.json, dict) is True
    assert response.json["bicycle_id"] == bicycle1_id


def test_get_user_orders(client):
    global user1_id
    response = client.get(f"api/v1/user/{user1_id}/order")
    assert response.status_code == 200
    assert isinstance(response.json, list) is True
    # json.response == [[[{json response}, status code]]]
    # TODO refactor return object
    assert response.json[0]["order_status"] == "Pending"
    assert response.json[0]["total_price"] == 400.0
    assert response.json[0]["user_id"] == user1_id


def test_update_order(client):
    global user_id
    global order1_id
    global bicycle1_id
    update_order_data = {
        "order_status": "Done",
        "total_price": 400,
        "bicycle_id": bicycle1_id,
        "user_id": user1_id,
    }
    response = client.put(
        f"api/v1/order/{order1_id}",
        data=json.dumps(update_order_data),
        content_type="application/json",
    )

    assert response.status_code == 200


def test_delete_order(client):
    global user_id
    global order1_id
    response = client.delete(f"api/v1/order/{order1_id}")
    assert response.status_code == 200
    assert isinstance(response.json, dict) is True
    client.delete(f"api/v1/user/{user1_id}")
