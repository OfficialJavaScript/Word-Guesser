#!/usr/bin/env python3

import requests

def generate_word(length):
    url = "https://random-word-api.vercel.app/api"
    params = {'words': 1, 'length': length, 'type': 'uppercase'}
    result = requests.get(url, params=params).json()[0]
    return result

if __name__ == ("__main__"):
    print("Don't run me, run main.py!")