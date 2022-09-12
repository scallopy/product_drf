import requests

# to display response in terminal
response = requests.get('http://127.0.0.1:8000/api_drinks/drinks_list/')
print(response.json())
