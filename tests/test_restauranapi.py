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


def test_remove_allitems_tableorders():
    tablenumber = 10
    desired_item_name = "Pasta"
    payload = payload_items([desired_item_name])
    create_order_response = create_orders(payload,tablenumber)
    assert create_order_response.status_code == 201

    list_orders_response = list_orders_by_tableid(tablenumber)
    assert list_orders_response.status_code == 200

    data = list_orders_response.json()
    # Check if the 'table_id' is 10
    assert data['table_id'] == tablenumber, "The table_id is not 10."

    # Check if any item has the desired 'item_name'
    for item in data['items']:
        if item['item_name'] == desired_item_name:
            found = True
            break
    else:
        assert found, f"The item {desired_item_name} was not found at table_id {tablenumber}."

    remove_order_response = delete_tableallorders(tablenumber)
    assert remove_order_response.status_code == 200

    list_orders_response = list_orders_by_tableid(tablenumber)
    assert list_orders_response.status_code == 404

    data = list_orders_response.json()

    assert "Table not found" in data['message']

def test_remove_specificitems_tableorder():
    tablenumber = 10
    desired_item_name = "Pasta"
    payload = payload_items([desired_item_name])
    create_order_response = create_orders(payload,tablenumber)
    assert create_order_response.status_code == 201

    list_orders_response = list_orders_by_tableid(tablenumber)
    assert list_orders_response.status_code == 200

    data = list_orders_response.json()
    # Check if the 'table_id' is 10
    assert data['table_id'] == tablenumber, "The table_id is not 10."

    # Check if any item has the desired 'item_name'
    for item in data['items']:
        if item['item_name'] == desired_item_name:
            found = True
            break
    else:
        assert found, f"The item {desired_item_name} was not found at table_id {tablenumber}."

    remove_order_response = delete_tableaitemorder(tablenumber, desired_item_name)
    assert remove_order_response.status_code == 200

    list_orders_response = list_orders_by_tableid(tablenumber)
    assert list_orders_response.status_code == 200

    data = list_orders_response.json()
    desired_item_name = 'Pasta'

    # Check if the 'table_id' is 10
    assert data['table_id'] == 10, "The table_id is not 10."

    # Iterate through the 'items' list and check if the desired item is present
    found = False
    for item in data['items']:
        if item.get('item_name') == desired_item_name:
            found = True
            break
    
    # Assert that the item was not found
    assert not found, f"The item {desired_item_name} was found at table_id 10."

    #assert "Table not found" in data['message']    

def create_orders(payload, tablenumber):
    return requests.post(ENDPOINT + f"/{tablenumber}", json=payload)

def list_orders():
    return requests.get(ENDPOINT )

def list_orders_by_tableid(table_id):
    return requests.get(ENDPOINT+f"/{table_id}" )

def update_order(payload):
    return requests.put(ENDPOINT, json=payload)

def delete_tableallorders(tablenumber):
    return requests.delete(ENDPOINT+ f"/{tablenumber}")

def delete_tableaitemorder(tablenumber, item_name):
    return requests.delete(ENDPOINT+ f"/{tablenumber}/{item_name}")

def payload_items(items):
    return {
        "items": items
    }