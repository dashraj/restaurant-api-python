import requests
import threading
import json

table_amount = 10
item_amount = 10
num_thread = 10

# Define the base URL of your Flask API
base_url = 'http://127.0.0.1:5000'  # Update with your API's URL

def run_client_add(thread_id):
    for table_id in range(0, table_amount):
        item_id_start = item_amount * thread_id
        item_id_end = item_amount * (thread_id + 1)

        for item_id in range(item_id_start, item_id_end):
            endpoint = f"/restaurant/{table_id}/{item_id}"
            url = f"{base_url}{endpoint}"
            
            # Send a POST request to add an item
            response = requests.post(url)
            
            if response.status_code != 200:
                print(f"Failed to add item to {endpoint}, status code: {response.status_code}")

def run_client_check_all():
    print("=== Checking ===")

    endpoint = f"/restaurant"
    url = f"{base_url}{endpoint}"
        
        # Send a GET request to query the table
    response = requests.get(url)
    data = response.json()
        
        # if len(data) != item_amount * num_thread:
        #     print(f"Table {table_id} has an incorrect amount of items")
        #     exit(1)

    print(data)

if __name__ == '__main__':
    threads = []

    print(f"Running {num_thread} threads...")
    print(f"Each thread adds {item_amount} items for each {table_amount} tables.")
    for i in range(0, num_thread):
        t = threading.Thread(target= run_client_add, args=(i,))
        threads.append(t)
        t.start()

    for i in range(0, num_thread):
        t = threads[i]
        t.join()

    run_client_check_all()
