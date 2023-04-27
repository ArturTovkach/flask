import requests

res = requests.post('http://127.0.0.1:3000/api/courses/3', {'name': 'Python', 'videos': 15})
res = requests.post('http://127.0.0.1:3000/api/courses/4', {'name': 'PHP', 'videos': 15})
print(res.json())
