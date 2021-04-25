import pip
pip install requests
import requests

url = "http://18.224.107.59:5000/"

response = requests.get(url)
print(response)
