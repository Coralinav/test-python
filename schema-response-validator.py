import requests
from jsonschema import validate

# Define the URL to retrieve data from
url = "https://jsonplaceholder.typicode.com/todos/2"

# Send a GET request to the URL and retrieve the response
response = requests.get(url)

# Parse the response data as JSON
responseJSON = response.json()

# Define a schema to validate the JSON data against
schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "completed": {"type": "boolean"},
    }
}

try:
    # Validate the JSON data against the schema
    validate(instance=responseJSON, schema=schema)
    print('Schema validation succeeded.')
except Exception as e:
    # Print an error message if the validation fails
    print(f'Schema validation failed with error: {e}')
