import requests
import yaml

# Define the API endpoint
api_url = 'https://example-api.com/data'
api_key = 'SEUNiTMcpNyXKXnnaNTz70pe0kWumpKrK2vVd0NGL51h3XVDXtZumw0CfVJST12uP3k0vrJPrXgiokerpIgWkHWzRcOTyWIdBdASAdp5nEsShs2EH6HUbgCJEx4NNBW6'



# Call the API with the Authorization header
response = requests.get(api_url, headers={'Authorization': f'Bearer {api_key}'})
data = response.json()

# Print the response data
print(data)
