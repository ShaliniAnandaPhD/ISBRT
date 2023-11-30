# external_api_integration.py
import requests
import json

def send_to_external_api(input_data, api_endpoint, headers):
    """
    Sends a request to an external API and returns the response.

    Parameters:
        input_data (dict): The data to be sent to the API.
        api_endpoint (str): The URL of the API endpoint.
        headers (dict): Headers to be sent along with the request.

    Returns:
        dict: The response from the API.
    """
    try:
        # Convert the input data to JSON format
        json_data = json.dumps(input_data)

        # Send a POST request to the API endpoint
        response = requests.post(api_endpoint, data=json_data, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Return the JSON response if successful
            return response.json()
        else:
            # Return a message if the request failed
            return {"error": f"Request failed with status code {response.status_code}"}
    except Exception as e:
        # Return an error message in case of an exception
        return {"error": str(e)}

# Example usage of the function (replace with your actual API details)
if __name__ == "__main__":
    api_url = "https://api.example.com/endpoint"  # Replace with your API's endpoint URL
    api_headers = {"Authorization": "Bearer YOUR_API_KEY"}  # Replace with your API's required headers
    input_data = {"data": "Example data"}  # Replace with the data you want to send

    response = send_to_external_api(input_data, api_url, api_headers)
    print(response)

