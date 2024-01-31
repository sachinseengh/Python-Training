import requests

api_url = "https://catfact.ninja/fact"


response = requests.get(api_url)


if(response.status_code == 200):
    print(response.json()["fact"])
    print(response.json()["length"])
    