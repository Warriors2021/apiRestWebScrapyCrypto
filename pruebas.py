import requests

url = "http://127.0.0.1:5000/price"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3NzEwNTE5MCwianRpIjoiZmVmNDI0ZTQtOTZjNS00OTAwLTliMTItYzA5YTc1YWZhN2FlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6OSwibmJmIjoxNjc3MTA1MTkwLCJleHAiOjE2NzcxMDYwOTB9.9-QzZ1jDW31pY-9DTW1zygo2fiB3di8EKcG3uiGzzfw"

headers = {
    "Authorization": f"{token}"
}

response = requests.get(url, headers=headers)

print(response.text)