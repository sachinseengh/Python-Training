import requests
from adviceclass import Advice

api_url = "https://api.adviceslip.com/advice"

response = requests.get(api_url)

print(response.status_code)

if(response.status_code== 200):
    # print(type(response.json()))
    # print(response.json()["slip"]["advice"])
    
    a = Advice(data=response.json());
    print(a.advice)
    

   
