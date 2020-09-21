import pandas as pd
import glassdoor_scraper as gs


# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 11:47:44 2020
@author: Ken
"""


path = "/Users/sungjbyun/ds_salary_prediction_project"

df = gs.get_jobs('data scientist', 1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index=False)
