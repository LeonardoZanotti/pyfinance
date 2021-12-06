#!/usr/bin/env python3
# Leonardo José Zanotti
# https://github.com/LeonardoZanotti/pyfinance

import matplotlib.pyplot as plt
import requests
from decouple import config

API_KEY = config("API_KEY")
COMPANY = config("COMPANY")         # FB, AAPL, MU, and other companies
TIME = config("TIME")

response = requests.get(
    f"https://financialmodelingprep.com/api/v3/income-statement/{COMPANY}?limit={TIME}&apikey={API_KEY}")

json_response = response.json()

revenues = list(reversed([json_response[i]['revenue']
                for i in range(len(json_response))]))
profits = list(reversed([json_response[i]['grossProfit']
               for i in range(len(json_response))]))

# graphic view
plt.plot(revenues, label="Revenue")
plt.plot(profits, label="Profit")
plt.title(f"{COMPANY} revenue and profit")
plt.legend(loc="upper left")
plt.show()


response = requests.get(
    f"https://financialmodelingprep.com/api/v3/income-statement/{COMPANY}?datatype=csv&limit={TIME}&apikey={API_KEY}")

# csv view
with open('data.csv', 'wb') as f:
    f.write(response.content)
f.close()
