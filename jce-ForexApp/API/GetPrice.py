__author__ = 'Oshri&Yaakov'
import requests
import json


def getprice():
    req = requests.get(url="https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22clm15.nym%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=")
    response = json.loads(req.content)
    return response["list"]["resources"][0]["resource"]["fields"]["price"]


