import requests

url =  "https://api.animechan.io/v1/quotes/random"

response = requests.get(url)
if response.status_code != 200:
    raise Exception("API request failed with status code {}".format(response.status_code))
else:
    data = response.json()["data"]

print(data["anime"] ["name"])