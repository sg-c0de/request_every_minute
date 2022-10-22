#!/usr/bin/env python

import time
import requests
import datetime
servers = ["maria.ru", "rose.ru", "sina.ru"]

starttime = time.time()
while True:
    now = datetime.datetime.now()
    for url in servers:
        req = requests.get("http://" + url)
        resp = req.json()
        print(now.strftime("%d/%m/%Y %H:%M:%S"), url, resp.get("count"))
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))
