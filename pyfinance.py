#!/usr/bin/env python3
# Leonardo José Zanotti
# https://github.com/LeonardoZanotti/pyfinance

from decouple import config

API_KEY = config("API_KEY")

print(API_KEY)
