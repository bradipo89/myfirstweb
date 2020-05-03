import requests

url = 'http://localhost:8080/results'
r = requests.post(url,json={'nome':'aa'})

print(r.json())
