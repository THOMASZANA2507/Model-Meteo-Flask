import requests
url = 'http://localhost:5000/api'
r = requests.post(url,json={'exp':X_test,})
print(r.json())
