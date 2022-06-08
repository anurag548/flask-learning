import  requests


BASE = "http://127.0.0.1:5000/"



respons = requests.put(BASE+"video/19",{"likes":"10"})
print(respons.json())