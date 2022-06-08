import  requests


BASE = "http://127.0.0.1:5000/"

datToSend = [{"likes":"100","name":"Test0","views":"123456"},{"likes":"100","name":"Test1","views":"12345678"},{"likes":"1000","name":"Test2","views":"123456789"},{"likes":"10000","name":"Test3","views":"1234567890"}]

for i in datToSend:
    requests.get(BASE+"video/"+s)
    # print(respons.json())
    
input()
respons = requests.get(BASE+"video/1")
print(respons.json())