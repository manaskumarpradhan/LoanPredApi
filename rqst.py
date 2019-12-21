# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 11:00:15 2019

@author: pradhma
"""

import requests
import json

#data = [{"Home":"a","Age":37,"Income":177,"Experience":18}]
#j_data = json.dumps(data)
#print(j_data)

#payload = [{"Home":"a","Age":32,"Income":150,"Experience":12}] #loan Approved
payload = [{"Home":"a","Age":30,"Income":148,"Experience":12}] #loan not Approved
#r = requests.post('http://127.0.0.1:5000/predict', json=payload)
r = requests.post('https://loan-approval-prediction-api.herokuapp.com/predict', json=payload)
print(r.status_code)
print(r.content)
print(type(r.content))
#print(int(json.loads(r.content)['prediction'][1]))
jss = json.loads(r.content)
print("jss is", jss)
pred = int(json.loads(r.content)['prediction'][1])
print(pred)

if pred==0:
    print("Loan not approved")
else:
    print("Loan Approved")
print(type(json.loads((r.content))))

