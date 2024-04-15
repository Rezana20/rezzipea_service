import pytest
import csv
import requests

# Fixture to set up and tear down the CSV file for testing
@pytest.fixture
def setup_csv_file():
    # Write initial data to the CSV file
    with open("../data/subscribers", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["John Doe", "johndoe@example.com"])
        writer.writerow(["Jane Smith", "janesmith@example.com"])
    yield
    # Remove the CSV file after the test
    import os
    os.remove("../data/subscribers")

# Test subscribing to newsletter
# def test_subscribe_to_newsletter(setup_csv_file):
#     url = "http://127.0.0.1:8000/newsletter/subscribe"
#     data = {"user_name": "Alice", "email": "alice@example.com"}
#     response = requests.post(url, json=data)
#     assert response.status_code == 200
#     assert response.json() == {"status": "success", "message": "Subscribed with alice@example.com"}
#
# # Test unsubscribing from newsletter
# def test_unsubscribe_from_newsletter(setup_csv_file):
#     url = "http://127.0.0.1:8000/newsletter/unsubscribe"
#     data = {"email": "janesmith@example.com"}
#     response = requests.post(url, json=data)
#     assert response.status_code == 200
#     assert response.json() == {"status": "success", "message": "We are sorry to see you leave. Unsubscribed from our content, from janesmith@example.com"}
