import json
import display
import history
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(script_dir, "time.json")

def checkIfPossible(data,name):
    if name in data:
        return True
    return False

def addTime(data,name,event,amount): # assummes name in data 
    data[name][0] += int(amount)
    data[name][1] = event
    history.addToLog((name,event,amount))

def quit(name):
    if name == "q":
        return True
    return False

def run():
    with open(FILE,"r") as f:
        data = json.load(f)
    name = input("Please give the name of the object or quit.\n")
    if quit(name):
        print("Exiting")
        return
    check = checkIfPossible(data,name)
    while not check:
        print()
        print("Error, this is not a tracked object. See list of objects below")
        display.run()
        name = input("Plese enter a new name or quit.\n") # MAYBE LIST POSSIBLE TRACKERS.
        if quit(name):
            print("Exiting")
            return
        check = checkIfPossible(data,name)

    print()

    event = input("Please enter the event you are logging or quit.\n")
    if quit(event):
        print("Exiting")
        return

    amount = input("Please give the amount of time in minutes or quit.\n")
    if quit(amount):
        print("Exiting")
        return
    amount = int(amount)

    addTime(data,name,event,amount)
    print("Time succesfully added.")
    with open(FILE,"w") as f:
        json.dump(data, f, indent=4)

### NOT INTERACTIVE
def runCLI(args):
    try:
        name,event,amount = args
        with open(FILE,"r") as f:
            data = json.load(f)
        check = checkIfPossible(data,name)
        if not check:
            print("ERROR. This object does not exist.")
        addTime(data,name,event,amount)
        print("Time succesfully added.")
        with open(FILE,"w") as f:
            json.dump(data, f, indent=4)
    except:
        print("ERROR. Incompatible amount of args")
        return 
