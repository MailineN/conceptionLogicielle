import requests 

url = "http://127.0.0.1:8000/"
req = requests.get(url+"/creer-un-deck/")
deck = req.json()

print(deck)