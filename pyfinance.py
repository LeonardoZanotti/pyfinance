#!/usr/bin/env python3
# Leonardo José Zanotti
# https://github.com/LeonardoZanotti/pyfinance

import matplotlib.pyplot as plt
import requests
from decouple import config

API_KEY = config("API_KEY")
COMPANY = config("COMPANY")
TIME = config("TIME")

response = requests.get(
    f"https://financialmodelingprep.com/api/v3/income-statement/{COMPANY}?limit={TIME}&apikey={API_KEY}")

json_response = response.json()

print(json_response)
