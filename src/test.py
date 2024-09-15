import requests


respose = requests.get('https://jsonplaceholder.typicode.com/users')

for data in respose.json():
    print(data.get('name'))