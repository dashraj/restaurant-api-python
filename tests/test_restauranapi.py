import requests
ENDPOINT = "http://localhost:5000/restaurant" 

def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_can_create_orders():
    mock_Items = "Pasta"
    payload = payload_items([mock_Items])
    tablenumber = 1
    create_order_response = create_orders(payload,tablenumber)
    assert create_order_response.status_code == 201

    list_orders_response = list_orders()
    assert list_orders_response.status_code == 200

    data = list_orders_response.json()
    for entry in data:
        if entry['table_id'] == tablenumber:
            for item in entry['items']:
                # Check if the 'item_name' matches the desired_item_name
                if item['item_name'] == mock_Items:
                    # Set the 'found' flag to True and break the loop
                    found = True
                    break

    # Assert that the item was found
    assert found, f"The item Pasta was not found at table_id 1."

def test_can_list_orders():
    list_orders_response = list_orders()
    assert list_orders_response.status_code == 200


def test_remove_items_tableorder():
    pass


def create_orders(payload, tablenumber):
    return requests.post(ENDPOINT + f"/{tablenumber}", json=payload)

def list_orders():
    return requests.get(ENDPOINT )

def update_task(payload):
    return requests.put(ENDPOINT, json=payload)

def payload_items(items):
    return {
        "items": items
    }