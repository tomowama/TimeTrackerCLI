import json
import collections
from datetime import date
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(script_dir, "history.json")


def addToLog(info):
    name,event,amount = info
    with open(FILE,"r") as f:
        data = json.load(f)
    log = data["log"]
    dq = collections.deque(log)
    today = str(date.today())
    newEntry = f"{today} || Object: {name}, Event: {event}, Time: {amount}"
    dq.append(newEntry)
    if len(dq) > 20:
        dq.popleft()
    data["log"] = list(dq)
    with open(FILE,"w") as f:
        json.dump(data, f, indent=4)
def run():
    with open(FILE,"r") as f:
        data = json.load(f)
    log = data["log"]
    for entry in log:
        print(entry)

