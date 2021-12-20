import json
import sys

data={
   "status": "SUCCESS",
   "device": [
         {
             "model":"XXXX-A",
             "username": "login1",
             "ip": "10.10.10.1",
             "password": "123",
             "device_type": "cisco_ios"
         },
         {
             "model":"XXXX-A",
             "username": "login2",
             "ip": "10.10.10.2",
             "password": "456",
             "device_type": "cisco_ios"
         },
         {
             "model":"XXXX-A",
             "username": "login3",
             "ip": "10.10.10.3",
             "password": "test",
             "device_type": "cisco_ios"
         }
    ]
}
json_str = json.dumps(data)
resp = json.loads(json_str)
print (resp['device'][0]['username'])
