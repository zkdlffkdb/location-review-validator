import requests
import json

# The URL of your running Flask server's predict endpoint
url = "http://127.0.0.1:5000/predict"

# Sample data to send to the API. 
# Make sure to include all the numerical features that the model expects.
sample_data = {
    "review_text": "this is a good place with excellent service.",
    "rating_person": 5.0,
    "main_category": "Restaurant",
    "can_claim": 1,
    "is_local_guide": 0,
    "sentiment_polarity": 0.8,
    "sentiment_subjectivity": 0.9
}

# Convert the data to a JSON string
json_data = json.dumps(sample_data)

# Set the headers to indicate that you are sending JSON data
headers = {
    "Content-Type": "application/json"
}

try:
    print("Sending POST request to the API...")
    # Send the POST request
    response = requests.post(url, data=json_data, headers=headers)
    
    # Check if the request was successful
    response.raise_for_status()
    
    # Print the JSON response from the server
    print("Response received:")
    print(response.json())

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
