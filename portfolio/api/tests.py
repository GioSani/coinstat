import json
import requests
import os

AUTH_ENDPOINT = 'http://127.0.0.1:8000/api/auth/login/'
PORTFOLIO_ENDPOINT = 'http://127.0.0.1:8000/api/portfolio/'
headers = {"content-type":"application/json"}
'''
data = {
    "username":"gio",
    "password":"g02071986",
}

r = requests.post(AUTH_ENDPOINT,data=data,headers=headers)
user = r.json()['user']
token = r.json()['token']
print type(token)
headers = {"content-type":"application/json",
                    "Authorization":"jwt "+ str(token),
           "user": user
            }
print headers
p = requests.get(PORTFOLIO_ENDPOINT,headers=headers)

print p.text
'''
data = {
    'username':'gio',
    'password':'g02071986',

}
headers = {"content-type":"application/json"}
r=requests.post(AUTH_ENDPOINT,data=json.dumps(data),headers=headers)
token = r.json()['token']
user = r.json()['user']
print user
print token
data = json.dumps({
    'content':'some new data'

})
headers = {"content-type":"application/json",
            "Authorization":"jwt "+str(token),
            "user":user,
}
data = json.dumps({
    "user":2,
    "coin_name":"bitcoin",
    "coin_quant": 6,
})
#r2=requests.get(ENDPOINT,data=data,headers=headers)
r2 = requests.get(PORTFOLIO_ENDPOINT,data=data,headers=headers)
print r2.text
