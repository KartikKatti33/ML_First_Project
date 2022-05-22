# -*- coding: utf-8 -*-
"""
Created on Sat May 21 18:08:49 2022

@author: karti
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Age':25, 'EstimatedSalary':25000 })

print(r.json())