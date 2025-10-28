import requests

x = requests.get("http://localhost:8091/")
print(x.json())