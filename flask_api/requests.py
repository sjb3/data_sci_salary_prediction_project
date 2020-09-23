# -*- coding: utf-8 -*-
"""
annot:
  Created on Tue Apr 14 08:45:56 2020
  @author: Ken
  https://github.com/PlayingNumbers/ds_salary_proj/blob/master/FlaskAPI/requests.py
"""

import requests
from data_input import data_in

URL = 'http: // 127.0.0.1: 5000/predict'
headers = {"Content-Type": "application/json"}
data = {"input": data_in}

r = requests.get(URL, headers=headers, json=data)

r.json()
