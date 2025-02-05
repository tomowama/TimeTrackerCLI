import json
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(script_dir, "time.json")
def convertTime(minutes):
    # want to convert to days / hours / minutes
    hours = minutes // 60 
    mins = minutes % 60
    days = hours // 24
    hrs = hours % 24
    return f"{days} days, {hrs} hours and, {mins} minutes"
def run():
    with open(FILE,"r") as f:
        data = json.load(f)
    print("These are the tracked objects and their time")
    for name in data:
        time = convertTime(data[name][0])
        mostRecentEvent = data[name][1]
        print(f"{name} : {time} || Last logged event: {mostRecentEvent}")



