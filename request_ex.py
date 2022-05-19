import requests
data=requests.get('https://www.hotstar.com')
if data.status_code == 200:
    print(data.text)