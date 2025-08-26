# app.py

from flask import Flask, request, jsonify
from model import predict as model_predict

# Create a Flask application
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    """
    API endpoint to make a prediction.
    Takes JSON input like: {"country": "France", "date": "2025-09-15"}
    """
    # Get the JSON data from the request
    data = request.get_json()
    
    # --- Input Validation ---
    if not data or 'country' not in data or 'date' not in data:
        return jsonify({"error": "Missing 'country' or 'date' in request"}), 400

    country = data['country']
    target_date = data['date']

    # --- Get Prediction ---
    try:
        prediction = model_predict(country, target_date)
        return jsonify(prediction)
    except Exception as e:
        # Log the error here in a real application
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the app on port 5000, accessible from any IP
    app.run(host='0.0.0.0', port=5000)
