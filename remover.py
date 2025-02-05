import json
import display
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(script_dir, "time.json")

def checkIfExist(data,name):
    if name in data:
        return True
    return False

def remove(data,name):
    del data[name]

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
    check = checkIfExist(data,name)
    while not check:
        print()
        print("Error this is not being tracked. See list of tracked objects below.")
        display.run()
        name = input("Please enter a new name or quit.\n")
        if quit(name):
            print("Exiting")
            return
        check = checkIfExist(data,name)
    print()
    remove(data,name)

    with open(FILE,"w") as f:
        json.dump(data,f,indent=4)
        

### NOT INTERACTIVE 
def runCLI(args):
    try:
        name = args[0]
        with open(FILE,"r") as f:
            data = json.load(f)
        check = checkIfExist(data,name)
        if not check:
            print("ERROR. This object does not exist.")
        remove(data,name)
        print("Object removed.")
        with open(FILE,"w") as f:
            json.dump(data,f,indent=4)
    except:
        print("ERROR. Incompatible amount of args.")

