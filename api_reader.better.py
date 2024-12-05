import requests
import yaml

# Read API key from the YAML file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)
api_key = config['api_key']
api_url = config['api_url']

# Call the API with the Authorization header
response = requests.get(api_url, headers={'Authorization': f'Bearer {api_key}'})
data = response.json()

# Print the response data
print(data)

# 