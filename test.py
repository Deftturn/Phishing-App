import requests

res = requests.get('https://phishing-app-41sr.onrender.com').content
print(res)