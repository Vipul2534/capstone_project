# test_app.py

from app import app
import json

def test_predict_endpoint():
    """
    Test the /predict endpoint for a successful response.
    """
    # Create a test client using the Flask application
    client = app.test_client()

    # Define the test input data
    test_data = {"country": "Germany", "date": "2025-10-20"}

    # Send a POST request to the /predict endpoint
    response = client.post('/predict', 
                           data=json.dumps(test_data), 
                           content_type='application/json')

    # --- Assertions ---
    # Check that the status code is 200 (OK)
    assert response.status_code == 200

    # Check that the response contains the key 'predicted_revenue'
    response_data = json.loads(response.data)
    assert 'predicted_revenue' in response_data
