import requests

try:
    x = requests.get("http://localhost:8091/")
    x.raise_for_status()
    print(x.json())
    
except requests.RequestException as e:
    print(f"Error fetching API: {e}")
    raise